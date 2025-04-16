from PyQt5.QtCore import QTimer

from handler.handler_ui import HandlerUI
from handler.handler_comm_umb import HandlerCommUMB
from handler.handler_plot import HandlerPlot
# from handler.handler_log import HandlerLog
from utils.data_types import DataUMB


class CoreController:
    def __init__(self):
        # ============================
        # UI 및 핸들러 초기화
        # ============================
        self.ui = HandlerUI()
        self.umb_handler = HandlerCommUMB(self)
        # self.log_handler = HandlerLog()

        # 플롯 핸들러 (Qt Designer에서 설정한 objectName 기준)
        self.plot_handler_cur_r = HandlerPlot(self.ui.PLOT_ROLL,  "Roll",  "deg")
        self.plot_handler_cur_p = HandlerPlot(self.ui.PLOT_PITCH, "Pitch", "deg")
        self.plot_handler_cur_y = HandlerPlot(self.ui.PLOT_YAW,   "Yaw",   "deg")

        # UI와 컨트롤러 연결
        self.ui.set_controller(self)

        # ============================
        # 데이터 저장소 및 타이머
        # ============================
        self.umb_data_history = []      # 수신된 데이터 누적 리스트
        self.last_plot_index = 0        # 마지막으로 plot에 반영한 데이터 인덱스

        # 10Hz Plot 업데이트 타이머
        self.plot_timer = QTimer()
        self.plot_timer.timeout.connect(self.update_plots)
        self.plot_timer.start(100)  # 100ms 간격

    def start(self):
        """UI 실행"""
        self.ui.show()

    def on_umb_data_received(self, data: DataUMB):
        """
        시리얼로부터 UMB 데이터 수신 시 호출됨
        → 데이터 저장, 로그, 그래프 갱신 트리거
        """
        # 데이터 저장 (최대 1000개 유지)
        self.umb_data_history.append(data)
        if len(self.umb_data_history) > 1000:
            self.umb_data_history.pop(0)
            self.last_plot_index = max(0, self.last_plot_index - 1)

        # TODO: 로그 핸들러로 전달
        # self.log_handler.append(data)

        # 디버그 출력
        print(f"[CORE] UMB Data received: {data.timestamp} | "
              f"RPY: {data.roll:.2f}, {data.pitch:.2f}, {data.yaw:.2f}")

    def update_plots(self):
        """
        10Hz 타이머에 의해 주기적으로 호출됨
        마지막으로 plot에 반영된 이후의 모든 데이터를 순차적으로 시각화
        """
        total_data = len(self.umb_data_history)

        # 새로운 데이터가 없다면 종료
        if self.last_plot_index >= total_data:
            return

        # 새로 들어온 데이터 모두 plot에 반영
        new_data_list = self.umb_data_history[self.last_plot_index:]
        for data in new_data_list:
            self.plot_handler_cur_r.update_plot(data.roll)
            self.plot_handler_cur_p.update_plot(data.pitch)
            self.plot_handler_cur_y.update_plot(data.yaw)

        # 마지막 인덱스 갱신
        self.last_plot_index = total_data

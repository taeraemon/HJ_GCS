from handler.handler_ui import HandlerUI
from handler.handler_comm_umb import HandlerCommUMB
# from handler.handler_plot import HandlerPlot
# from handler.handler_log import HandlerLog
from utils.data_types import DataUMB

class CoreController:
    def __init__(self):
        # UI 초기화
        self.ui = HandlerUI()

        # 핸들러 초기화
        self.umb_handler = HandlerCommUMB(self)
        # self.plot_handler = HandlerPlot(self.ui)
        # self.log_handler = HandlerLog()

        # UI에 컨트롤러 연결
        self.ui.set_controller(self)

        # 데이터 저장소 예시
        self.umb_data_history = []

    def start(self):
        self.ui.show()

    def on_umb_data_received(self, data: DataUMB):
        """
        handler_comm_umb.py에서 데이터를 파싱한 뒤 이 메서드로 전달함
        여기에 로그 저장, 그래프 업데이트 등 처리 추가
        """
        # 데이터 저장 (예: 최근 1000개 유지)
        self.umb_data_history.append(data)
        if len(self.umb_data_history) > 1000:
            self.umb_data_history.pop(0)

        # TODO: 로그 핸들러로 전달
        # self.log_handler.append(data)

        # TODO: 플롯 핸들러로 전달
        # self.plot_handler.update(data)

        # 일단 콘솔에 출력
        print(f"[CORE] UMB Data received: {data.timestamp} | RPY: {data.roll:.2f}, {data.pitch:.2f}, {data.yaw:.2f}")

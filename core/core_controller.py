from PyQt5.QtCore import QTimer
from datetime import datetime

from handler.handler_ui import HandlerUI
from handler.handler_comm_umb import HandlerCommUMB
from handler.handler_comm_tlm import HandlerCommTLM
from handler.handler_comm_gse import HandlerCommGSE
from handler.handler_plot import HandlerPlot
# from handler.handler_log import HandlerLog
from utils.data_types import DataVehicle


class CoreController:
    def __init__(self):
        # ============================
        # UI 및 핸들러 초기화
        # ============================
        self.ui = HandlerUI()
        self.umb_handler = HandlerCommUMB(self)
        self.tlm_handler = HandlerCommTLM(self)
        self.gse_handler = HandlerCommGSE(self)
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
        # 마지막 수신된 데이터 저장
        self.last_umb_data = None
        self.last_tlm_data = None
        self.last_vehicle_data = None

        # 모든 데이터를 각각 저장
        self.umb_data_history = []  # UMB 데이터 저장 리스트
        self.tlm_data_history = []  # TLM 데이터 저장 리스트
        self.vehicle_data_history = []  # 통합된 데이터 저장 리스트 (GUI 업데이트용)
        self.last_plot_index = 0        # 마지막으로 plot에 반영한 데이터 인덱스

        # 데이터 소스 관리 변수 - 기본값을 'UMB'로 설정
        self.active_source = 'UMB'
        
        # 플롯 업데이트 타이머 설정 (10Hz)
        self.plot_timer = QTimer()
        self.plot_timer.timeout.connect(self.update_plots)
        self.plot_timer.start(100)  # 100ms = 10Hz

    def start(self):
        """UI 실행"""
        self.ui.show()

    def on_umb_data_received(self, data: DataVehicle):
        """
        시리얼로부터 UMB 데이터 수신 시 호출됨
        → 모든 데이터는 저장하고, rate에 따라 GUI 업데이트 여부 결정
        """
        # 데이터 저장 - 항상 저장
        self.last_umb_data = data
        self.umb_data_history.append(data)
        
        # 데이터 로깅 - 항상 로깅
        self._log_data(data, 'UMB')
        
        # UMB 데이터 최대 개수 제한
        if len(self.umb_data_history) > 1000:
            self.umb_data_history.pop(0)
        
        # 디버그 출력
        self._append_vehicle_status(f"[CORE] UMB Data received: {data.timestamp} | "
                                  f"RPY: {data.nav_roll:.2f}, {data.nav_pitch:.2f}, {data.nav_yaw:.2f}")
              
        # 현재 액티브 소스가 UMB면 데이터 처리 (GUI 업데이트)
        if self.active_source == 'UMB':
            # GUI 업데이트 
            self.process_vehicle_data(data)

    def on_tlm_data_received(self, data: DataVehicle):
        """
        무선 텔레메트리로부터 TLM 데이터 수신 시 호출됨
        → 모든 데이터는 저장하고, rate에 따라 GUI 업데이트 여부 결정
        """
        # 데이터 저장 - 항상 저장
        self.last_tlm_data = data
        self.tlm_data_history.append(data)
        
        # 데이터 로깅 - 항상 로깅
        self._log_data(data, 'TLM')
        
        # TLM 데이터 최대 개수 제한
        if len(self.tlm_data_history) > 1000:
            self.tlm_data_history.pop(0)
        
        # 디버그 출력
        self._append_vehicle_status(f"[CORE] TLM Data received: {data.timestamp} | "
                                  f"RPY: {data.nav_roll:.2f}, {data.nav_pitch:.2f}, {data.nav_yaw:.2f}")
              
        # 현재 액티브 소스가 TLM이면 데이터 처리 (GUI 업데이트)
        if self.active_source == 'TLM':
            # GUI 업데이트
            self.process_vehicle_data(data)

    def on_gse_data_received(self, data):
        # GSE 데이터 처리
        self._append_vehicle_status(f"[CORE] GSE Data received: {data.timestamp} | "
                                  f"RPY: {data.roll:.2f}, {data.pitch:.2f}, {data.yaw:.2f}")
        pass

    def _log_data(self, data, source):
        """
        모든 데이터를 로깅하는 내부 메서드
        실제 로깅 구현은 추후 추가
        """
        # TODO: 실제 로깅 구현
        # 잠시 주석처리: self.log_handler.append(data, source)
        pass
    
    def process_vehicle_data(self, vehicle_data):
        """
        통합된 DataVehicle 처리 - 데이터 관리
        수신된 데이터를 vehicle_data_history에 저장하는 역할
        실제 GUI 업데이트는 타이머에 의해 update_plots에서 처리됨
        """
        # 마지막 데이터 저장
        self.last_vehicle_data = vehicle_data
        
        # 데이터 저장 (최대 1000개 유지)
        self.vehicle_data_history.append(vehicle_data)
        if len(self.vehicle_data_history) > 1000:
            self.vehicle_data_history.pop(0)
            self.last_plot_index = max(0, self.last_plot_index - 1)

    def update_plots(self):
        """
        10Hz 타이머에 의해 주기적으로 호출됨
        - 새로운 데이터를 모두 plot에 반영
        - 3D 자세 시각화 업데이트
        마지막으로 plot에 반영된 이후의 모든 데이터를 순차적으로 시각화
        """
        total_data = len(self.vehicle_data_history)

        # 새로운 데이터가 없다면 종료
        if self.last_plot_index >= total_data:
            return

        # 새로 들어온 데이터 모두 plot에 반영
        new_data_list = self.vehicle_data_history[self.last_plot_index:]
        for data in new_data_list:
            self.plot_handler_cur_r.update_plot(data.nav_roll)
            self.plot_handler_cur_p.update_plot(data.nav_pitch)
            self.plot_handler_cur_y.update_plot(data.nav_yaw)

        # 마지막 인덱스 갱신
        self.last_plot_index = total_data
        
        # 가장 최신 데이터로 3D 자세 시각화 업데이트
        if self.last_vehicle_data:
            self.ui.update_attitude(
                self.last_vehicle_data.nav_roll,
                self.last_vehicle_data.nav_pitch,
                self.last_vehicle_data.nav_yaw
            )

    def get_umb_data_history(self):
        """UMB 데이터 히스토리 반환 (로그 저장 등에 활용)"""
        return self.umb_data_history
    
    def get_tlm_data_history(self):
        """TLM 데이터 히스토리 반환 (로그 저장 등에 활용)"""
        return self.tlm_data_history
    
    def get_vehicle_data_history(self):
        """GUI에 사용된 데이터 히스토리 반환"""
        return self.vehicle_data_history
    
    def get_active_source(self):
        """현재 사용 중인 데이터 소스 반환"""
        return self.active_source

    def set_active_source(self, source):
        """
        UI 소스 버튼 클릭 시 호출될 메서드
        액티브 소스를 변경하고 UI를 업데이트함
        """
        if source in ['UMB', 'TLM']:
            self.active_source = source
            self._append_debug_message(f"[CORE] Active Source changed to: {source}")
            
            # 마지막 수신된 데이터가 있으면 바로 UI 업데이트
            if source == 'UMB' and self.last_umb_data:
                self.process_vehicle_data(self.last_umb_data)
            elif source == 'TLM' and self.last_tlm_data:
                self.process_vehicle_data(self.last_tlm_data)

    def _append_debug_message(self, line):
        """
        TE_GCS_DEBUG에 한 줄씩 출력 (최대 100줄 유지)
        """
        text_edit = self.ui.TE_GCS_DEBUG
        existing_text = text_edit.toPlainText()
        lines = existing_text.split('\n')

        if len(lines) >= 100:
            lines = lines[-99:]

        curr_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        lines.append(f"{curr_time} : {line}")

        text_edit.setPlainText('\n'.join(lines).strip())
        text_edit.verticalScrollBar().setValue(text_edit.verticalScrollBar().maximum())

    def _append_vehicle_status(self, line):
        """
        TE_VEHICLE_STATUS에 한 줄씩 출력 (최대 100줄 유지)
        """
        text_edit = self.ui.TE_VEHICLE_STATUS
        existing_text = text_edit.toPlainText()
        lines = existing_text.split('\n')

        if len(lines) >= 100:
            lines = lines[-99:]

        curr_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        lines.append(f"{curr_time} : {line}")

        text_edit.setPlainText('\n'.join(lines).strip())
        text_edit.verticalScrollBar().setValue(text_edit.verticalScrollBar().maximum())

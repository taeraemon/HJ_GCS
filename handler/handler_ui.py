from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5 import uic
from PyQt5.QtSerialPort import QSerialPortInfo
import os
from handler.handler_plot_3d import HandlerPlot3D

# ===== UI 파일 로딩 =====
UI_PATH = os.path.join(os.path.dirname(__file__), "../VFCommandCenter.ui")
form_class = uic.loadUiType(UI_PATH)[0]

# ===== UI 핸들러 클래스 =====
class HandlerUI(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.setFixedSize(1920, 1080)

        self.controller = None    # CoreController 연결용
        self._connect_ui_events() # 버튼 클릭 등 이벤트 연결
        self.refresh_umb_ports()  # 프로그램 시작 시 1회 호출
        self.refresh_tlm_ports()  # TLM 포트 목록 갱신
        self.refresh_gse_ports()  # GSE 포트 목록 갱신

        # 3D 자세 시각화 추가
        self.attitude_visualizer = HandlerPlot3D()
        # openGLWidget을 3D 자세 시각화로 대체
        container = QWidget()
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.addWidget(self.attitude_visualizer)
        
        # tabWidget의 tab_2에 있는 openGLWidget을 제거하고 새 컨테이너로 대체
        for i in range(self.tabWidget.count()):
            if self.tabWidget.tabText(i) == "Tab 2":
                tab = self.tabWidget.widget(i)
                old_geo = self.openGLWidget.geometry()
                self.openGLWidget.setParent(None)
                container.setGeometry(old_geo)
                container.setParent(tab)
                break

    # ===== 컨트롤러 연결 함수 =====
    def set_controller(self, controller):
        self.controller = controller

    # ===== UI 이벤트 연결 함수 (내부용) =====
    def _connect_ui_events(self):
        self.PB_UMB_SER_CONN.clicked.connect(self.on_umb_serial_connect_clicked)
        self.PB_UMB_SER_REFRESH.clicked.connect(self.refresh_umb_ports)
        self.PB_TLM_SER_CONN.clicked.connect(self.on_tlm_serial_connect_clicked)
        self.PB_TLM_SER_REFRESH.clicked.connect(self.refresh_tlm_ports)
        self.PB_GSE_SER_CONN.clicked.connect(self.on_gse_serial_connect_clicked)
        self.PB_GSE_SER_REFRESH.clicked.connect(self.refresh_gse_ports)

        # 버튼 초기 상태 설정
        self.PB_UMB_SER_CONN.setCheckable(True)
        self.PB_TLM_SER_CONN.setCheckable(True)
        self.PB_GSE_SER_CONN.setCheckable(True)

    # ===== UMB 시리얼 연결 처리 =====
    def on_umb_serial_connect_clicked(self):
        if self.controller:
            if self.PB_UMB_SER_CONN.isChecked():
                port = self.CB_UMB_SER_PORT.currentData()
                baud = int(self.LE_UMB_SER_BAUD.text())
                success = self.controller.umb_handler.connect_serial(port, baud)
                if not success:
                    self.PB_UMB_SER_CONN.setChecked(False)
            else:
                self.controller.umb_handler.connect_serial("", 0)  # 연결 해제

    # ===== TLM 시리얼 연결 처리 =====
    def on_tlm_serial_connect_clicked(self):
        if self.controller:
            if self.PB_TLM_SER_CONN.isChecked():
                port = self.CB_TLM_SER_PORT.currentData()
                baud = int(self.LE_TLM_SER_BAUD.text())
                success = self.controller.tlm_handler.connect_serial(port, baud)
                if not success:
                    self.PB_TLM_SER_CONN.setChecked(False)
            else:
                self.controller.tlm_handler.connect_serial("", 0)  # 연결 해제

    # ===== GSE 시리얼 연결 처리 =====
    def on_gse_serial_connect_clicked(self):
        if self.controller:
            if self.PB_GSE_SER_CONN.isChecked():
                port = self.CB_GSE_SER_PORT.currentData()
                baud = int(self.LE_GSE_SER_BAUD.text())
                success = self.controller.gse_handler.connect_serial(port, baud)
                if not success:
                    self.PB_GSE_SER_CONN.setChecked(False)
            else:
                self.controller.gse_handler.connect_serial("", 0)  # 연결 해제

    # ===== UMB 시리얼 포트 목록 갱신 =====
    def refresh_umb_ports(self):
        self.CB_UMB_SER_PORT.clear()
        port_list = QSerialPortInfo.availablePorts()
        for port in port_list:
            self.CB_UMB_SER_PORT.addItem(f"{port.portName()} - {port.description()}", port.portName())
        if not port_list:
            self.CB_UMB_SER_PORT.addItem("No Ports")

    # ===== TLM 시리얼 포트 목록 갱신 =====
    def refresh_tlm_ports(self):
        self.CB_TLM_SER_PORT.clear()
        port_list = QSerialPortInfo.availablePorts()
        for port in port_list:
            self.CB_TLM_SER_PORT.addItem(f"{port.portName()} - {port.description()}", port.portName())
        if not port_list:
            self.CB_TLM_SER_PORT.addItem("No Ports")

    # ===== GSE 시리얼 포트 목록 갱신 =====
    def refresh_gse_ports(self):
        self.CB_GSE_SER_PORT.clear()
        port_list = QSerialPortInfo.availablePorts()
        for port in port_list:
            self.CB_GSE_SER_PORT.addItem(f"{port.portName()} - {port.description()}", port.portName())
        if not port_list:
            self.CB_GSE_SER_PORT.addItem("No Ports")

    def update_attitude(self, roll, pitch, yaw):
        """자세 데이터를 업데이트하고 3D 시각화를 갱신합니다."""
        self.attitude_visualizer.update_attitude(roll, pitch, yaw)

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5.QtSerialPort import QSerialPortInfo
import os

# ===== UI 파일 로딩 =====
UI_PATH = os.path.join(os.path.dirname(__file__), "../VFCommandCenter.ui")
form_class = uic.loadUiType(UI_PATH)[0]

# ===== UI 핸들러 클래스 =====
class HandlerUI(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1400, 900)

        self.controller = None    # CoreController 연결용
        self._connect_ui_events() # 버튼 클릭 등 이벤트 연결
        self.refresh_umb_ports()  # 프로그램 시작 시 1회 호출

    # ===== 컨트롤러 연결 함수 =====
    def set_controller(self, controller):
        self.controller = controller

    # ===== UI 이벤트 연결 함수 (내부용) =====
    def _connect_ui_events(self):
        self.PB_UMB_SER_CONN.clicked.connect(self.on_umb_serial_connect_clicked)
        self.PB_UMB_SER_REFRESH.clicked.connect(self.refresh_umb_ports)

    # ===== UMB 시리얼 연결 처리 =====
    def on_umb_serial_connect_clicked(self):
        if self.controller:
            port = self.CB_UMB_SER_PORT.currentData()
            baud = int(self.LE_UMB_SER_BAUD.text())
            success = self.controller.umb_handler.connect_serial(port, baud)
            if success:
                self.PB_UMB_SER_CONN.setText("Connected!")
            else:
                self.PB_UMB_SER_CONN.setText("Connect\nSerial")

    # ===== UMB 시리얼 포트 목록 갱신 =====
    def refresh_umb_ports(self):
        self.CB_UMB_SER_PORT.clear()
        port_list = QSerialPortInfo.availablePorts()
        for port in port_list:
            # self.CB_UMB_SER_PORT.addItem(port.portName())
            self.CB_UMB_SER_PORT.addItem(f"{port.portName()} - {port.description()}", port.portName())
        if not port_list:
            self.CB_UMB_SER_PORT.addItem("No Ports")

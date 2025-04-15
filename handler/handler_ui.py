from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
import os

UI_PATH = os.path.join(os.path.dirname(__file__), "../VFCommandCenter.ui")
form_class = uic.loadUiType(UI_PATH)[0]

class HandlerUI(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1400, 900)

        self.controller = None
        self._connect_ui_events()

    def set_controller(self, controller):
        self.controller = controller

    def _connect_ui_events(self):
        # 버튼, 슬라이더 등의 시그널 연결 예시
        # self.myButton.clicked.connect(self.on_my_button_clicked)
        pass

    # def on_my_button_clicked(self):
    #     if self.controller:
    #         self.controller.do_something()

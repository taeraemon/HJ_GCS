from PyQt5.QtWidgets import QPushButton

class HandlerButton:
    def __init__(self, button_widget):
        """
        button_widget: QPushButton 인스턴스
        """
        self.button = button_widget

    def update_color(self, state):
        """
        QPushButton의 배경색을 상태에 따라 변경
        state: 0이면 빨간색, 1이면 초록색
        """
        color = "green" if state == 1 else "red"
        self.button.setStyleSheet(f"background-color: {color};")

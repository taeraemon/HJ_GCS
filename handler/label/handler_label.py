# handler/handler_label.py

class HandlerLabel:
    def __init__(self, label_widget, fmt="{:}"):
        """
        label_widget: QLabel 인스턴스
        fmt: 출력 포맷 (예: "{:.2f}°", "{:.3f} m", "{} sats")
        """
        self.label = label_widget
        self.fmt = fmt

    def update(self, value):
        """
        QLabel에 값을 포맷하여 출력
        """
        try:
            self.label.setText(self.fmt.format(value))
        except Exception as e:
            self.label.setText("ERR")

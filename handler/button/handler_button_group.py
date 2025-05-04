from handler.button.handler_button import HandlerButton
from PyQt5.QtWidgets import QWidget

class HandlerButtonGroup:
    def __init__(self, ui: QWidget):
        self.handlers = {
            "PB_PNID_SV_1": HandlerButton(ui.PB_PNID_SV_1),
            "PB_PNID_SV_2": HandlerButton(ui.PB_PNID_SV_2),
            "PB_PNID_SV_3": HandlerButton(ui.PB_PNID_SV_3),
            "PB_PNID_SV_4": HandlerButton(ui.PB_PNID_SV_4),
            "PB_PNID_SV_5": HandlerButton(ui.PB_PNID_SV_5),
            "PB_PNID_SV_6": HandlerButton(ui.PB_PNID_SV_6),
            "PB_PNID_SV_7": HandlerButton(ui.PB_PNID_SV_7),
            "PB_PNID_SV_8": HandlerButton(ui.PB_PNID_SV_8),
        }

    def update_all(self, data):
        # Update QPushButton colors based on data.sv
        for i, state in enumerate(data.sv):
            label_name = f"PB_PNID_SV_{i+1}"
            if label_name in self.handlers:
                self.handlers[label_name].update_color(state)

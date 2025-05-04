# handler/label/handler_label_group.py
from handler.label.handler_label import HandlerLabel
from PyQt5.QtWidgets import QWidget
from utils.data_types import DataVehicle

class HandlerLabelGroup:
    def __init__(self, ui: QWidget):
        self.handlers = {
            "gps_lat": HandlerLabel(ui.LB_GPS_LAT, "{:.6f}"),
            "gps_lon": HandlerLabel(ui.LB_GPS_LON, "{:.6f}"),
            "gps_alt": HandlerLabel(ui.LB_GPS_ALT, "{:.2f} m"),
            "gps_sat": HandlerLabel(ui.LB_GPS_SAT, "{} sats"),
            "LB_PNID_PT_1": HandlerLabel(ui.LB_PNID_PT_1, "{:.2f}"),
            "LB_PNID_PT_2": HandlerLabel(ui.LB_PNID_PT_2, "{:.2f}"),
            "LB_PNID_PT_3": HandlerLabel(ui.LB_PNID_PT_3, "{:.2f}"),
            "LB_PNID_PT_4": HandlerLabel(ui.LB_PNID_PT_4, "{:.2f}"),
            "LB_PNID_PT_5": HandlerLabel(ui.LB_PNID_PT_5, "{:.2f}"),
            "LB_PNID_PT_6": HandlerLabel(ui.LB_PNID_PT_6, "{:.2f}"),
            "LB_PNID_PT_7": HandlerLabel(ui.LB_PNID_PT_7, "{:.2f}"),
            "LB_PNID_PT_8": HandlerLabel(ui.LB_PNID_PT_8, "{:.2f}"),
            "LB_PNID_PT_9": HandlerLabel(ui.LB_PNID_PT_9, "{:.2f}"),
            "LB_PNID_PT_10": HandlerLabel(ui.LB_PNID_PT_10, "{:.2f}"),
            "LB_PNID_PT_11": HandlerLabel(ui.LB_PNID_PT_11, "{:.2f}"),
            "LB_PNID_PT_12": HandlerLabel(ui.LB_PNID_PT_12, "{:.2f}"),
            "LB_PNID_TC_1": HandlerLabel(ui.LB_PNID_TC_1, "{:.2f}"),
            "LB_PNID_TC_2": HandlerLabel(ui.LB_PNID_TC_2, "{:.2f}"),
            "LB_PNID_TC_3": HandlerLabel(ui.LB_PNID_TC_3, "{:.2f}"),
            "LB_PNID_TC_4": HandlerLabel(ui.LB_PNID_TC_4, "{:.2f}"),
            "LB_PNID_TC_5": HandlerLabel(ui.LB_PNID_TC_5, "{:.2f}"),
            "LB_PNID_TC_6": HandlerLabel(ui.LB_PNID_TC_6, "{:.2f}"),
            "LB_PNID_TC_7": HandlerLabel(ui.LB_PNID_TC_7, "{:.2f}"),
            "LB_PNID_TC_8": HandlerLabel(ui.LB_PNID_TC_8, "{:.2f}"),
            "LB_PNID_TC_9": HandlerLabel(ui.LB_PNID_TC_9, "{:.2f}"),
            "LB_PNID_TC_10": HandlerLabel(ui.LB_PNID_TC_10, "{:.2f}"),
        }

    def update_all(self, data: DataVehicle):
        self.handlers["gps_lat"].update(data.gps_lat)
        self.handlers["gps_lon"].update(data.gps_lon)
        self.handlers["gps_alt"].update(data.gps_alt)
        self.handlers["gps_sat"].update(data.gps_sat)

        # Update QLabel values based on data.pt
        for i, value in enumerate(data.pt):
            label_name = f"LB_PNID_PT_{i+1}"
            if label_name in self.handlers:
                self.handlers[label_name].update(value)

        # Update QLabel values based on data.tc
        for i, value in enumerate(data.tc):
            label_name = f"LB_PNID_TC_{i+1}"
            if label_name in self.handlers:
                self.handlers[label_name].update(value)

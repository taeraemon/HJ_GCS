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
        }

    def update_all(self, data: DataVehicle):
        self.handlers["gps_lat"].update(data.gps_lat)
        self.handlers["gps_lon"].update(data.gps_lon)
        self.handlers["gps_alt"].update(data.gps_alt)
        self.handlers["gps_sat"].update(data.gps_sat)

# handler/plot/handler_plot_group.py
from handler.plot.handler_plot import HandlerPlot
from PyQt5.QtWidgets import QWidget
from utils.data_types import DataVehicle

class HandlerPlotGroup:
    def __init__(self, ui: QWidget):
        self.handlers = {
            "nav_roll": HandlerPlot(ui.PLOT_NAV_ROLL, "Roll",  "deg", data_field="nav_roll"),
            "nav_pitch": HandlerPlot(ui.PLOT_NAV_PITCH, "Pitch", "deg", data_field="nav_pitch"),
            "nav_yaw": HandlerPlot(ui.PLOT_NAV_YAW,   "Yaw",   "deg", data_field="nav_yaw"),

            "imu_gyr_x": HandlerPlot(ui.PLOT_IMU_GYR_X, "Gyro X", "rad/s", data_field="imu_gyr_x"),
            "imu_gyr_y": HandlerPlot(ui.PLOT_IMU_GYR_Y, "Gyro Y", "rad/s", data_field="imu_gyr_y"),
            "imu_gyr_z": HandlerPlot(ui.PLOT_IMU_GYR_Z, "Gyro Z", "rad/s", data_field="imu_gyr_z"),

            "imu_acc_x": HandlerPlot(ui.PLOT_IMU_ACC_X, "Acc X", "m/s²", data_field="imu_acc_x"),
            "imu_acc_y": HandlerPlot(ui.PLOT_IMU_ACC_Y, "Acc Y", "m/s²", data_field="imu_acc_y"),
            "imu_acc_z": HandlerPlot(ui.PLOT_IMU_ACC_Z, "Acc Z", "m/s²", data_field="imu_acc_z"),
        }

    def update_plot_from_history_all(self, data_list: list[DataVehicle]):
        self.handlers["nav_roll"].update_plot_from_history(data_list)
        self.handlers["nav_pitch"].update_plot_from_history(data_list)
        self.handlers["nav_yaw"].update_plot_from_history(data_list)

        self.handlers["imu_gyr_x"].update_plot_from_history(data_list)
        self.handlers["imu_gyr_y"].update_plot_from_history(data_list)
        self.handlers["imu_gyr_z"].update_plot_from_history(data_list)

        self.handlers["imu_acc_x"].update_plot_from_history(data_list)
        self.handlers["imu_acc_y"].update_plot_from_history(data_list)
        self.handlers["imu_acc_z"].update_plot_from_history(data_list)

# handler/plot/handler_plot_group.py
from handler.plot.handler_plot import HandlerPlot
from PyQt5.QtWidgets import QWidget
from utils.data_types import DataVehicle

class HandlerPlotGroup:
    def __init__(self, ui: QWidget):
        self.handlers = {
            "nav_roll": HandlerPlot(ui.PLOT_NAV_ROLL,  "Roll",  "deg"),
            "nav_pitch": HandlerPlot(ui.PLOT_NAV_PITCH, "Pitch", "deg"),
            "nav_yaw": HandlerPlot(ui.PLOT_NAV_YAW,   "Yaw",   "deg"),

            "imu_gyr_x": HandlerPlot(ui.PLOT_IMU_GYR_X, "Gyro X", "rad/s"),
            "imu_gyr_y": HandlerPlot(ui.PLOT_IMU_GYR_Y, "Gyro Y", "rad/s"),
            "imu_gyr_z": HandlerPlot(ui.PLOT_IMU_GYR_Z, "Gyro Z", "rad/s"),

            "imu_acc_x": HandlerPlot(ui.PLOT_IMU_ACC_X, "Acc X", "m/s²"),
            "imu_acc_y": HandlerPlot(ui.PLOT_IMU_ACC_Y, "Acc Y", "m/s²"),
            "imu_acc_z": HandlerPlot(ui.PLOT_IMU_ACC_Z, "Acc Z", "m/s²"),
        }

    def update_all(self, data: DataVehicle):
        self.handlers["nav_roll"].update_plot(data.nav_roll)
        self.handlers["nav_pitch"].update_plot(data.nav_pitch)
        self.handlers["nav_yaw"].update_plot(data.nav_yaw)

        self.handlers["imu_gyr_x"].update_plot(data.imu_gyr_x)
        self.handlers["imu_gyr_y"].update_plot(data.imu_gyr_y)
        self.handlers["imu_gyr_z"].update_plot(data.imu_gyr_z)

        self.handlers["imu_acc_x"].update_plot(data.imu_acc_x)
        self.handlers["imu_acc_y"].update_plot(data.imu_acc_y)
        self.handlers["imu_acc_z"].update_plot(data.imu_acc_z)

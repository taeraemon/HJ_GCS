import pyqtgraph as pg
from utils.data_types import DataVehicle
from pyqtgraph import DateAxisItem
import time

class HandlerPlot:
    def __init__(self, plot_widget, title, unit=None, window=500, data_field=None):
        self.window = window
        self.data_field = data_field

        self.plot_widget = plot_widget
        self.plot_widget.setBackground('w')

        self.axis_left = pg.AxisItem(orientation='left')
        self.axis_left.setLabel(title, units=unit)
        self.axis_left.enableAutoSIPrefix(False)

        self.plot_widget.setAxisItems({'left': self.axis_left})
        self.plot_widget.setLabel('bottom', 'Samples')
        self.plot_widget.getAxis('bottom').setStyle(showValues=False)

        # self.plot_widget.showGrid(x=True, y=True)
        # self.plot_widget.setYRange(-45, 45)

        self.curve = self.plot_widget.plot(pen='b')

        # class 내부 초기화용
        self._last_plot_time = time.time()  # 처음엔 대충 현재시간

    def update_plot_from_history(self, data_list: list[DataVehicle]):
        # 최근 100개만 사용
        recent_data = data_list[-self.window:]

        # 타이틀에 따라 해당 속성 추출
        y_data = [getattr(d, self.data_field) for d in recent_data]

        x_data = list(range(len(y_data)))

        self.curve.setData(x_data, y_data)



# TODO : plot clear method
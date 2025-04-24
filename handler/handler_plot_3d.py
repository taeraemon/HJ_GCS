# handler/handler_plot_3d.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout
import pyqtgraph.opengl as gl
import numpy as np

class HandlerPlot3D(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # 레이아웃 설정
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        
        # GL View 위젯 생성 및 설정
        self.view = gl.GLViewWidget()
        layout.addWidget(self.view)
        self.view.setCameraPosition(distance=10)
        
        # 3D 축 표시
        self.axis = gl.GLAxisItem()
        self.view.addItem(self.axis)
        
        # 원기둥 모델
        z = np.linspace(-1, 1, 100)
        theta = np.linspace(0, 2 * np.pi, 100)
        z, theta = np.meshgrid(z, theta)
        x = np.cos(theta)
        y = np.sin(theta)
        
        faces = []
        for i in range(len(z) - 1):
            for j in range(len(theta) - 1):
                faces.append([i * len(theta) + j, (i + 1) * len(theta) + j, i * len(theta) + (j + 1)])
                faces.append([(i + 1) * len(theta) + j, (i + 1) * len(theta) + (j + 1), i * len(theta) + (j + 1)])
        
        meshdata = gl.MeshData(vertexes=np.array([x.flatten(), y.flatten(), z.flatten()]).T, faces=np.array(faces))
        self.cylinder = gl.GLMeshItem(meshdata=meshdata, smooth=True, color=(1, 0, 0, 0.5), shader='shaded')
        self.view.addItem(self.cylinder)
        
        # 세계 좌표계에 고정된 축 추가
        world_axis_length = 2
        self.world_x_axis = gl.GLLinePlotItem(pos=np.array([[0, 0, 0], [world_axis_length, 0, 0]]), color=(1, 0, 0, 1), width=2, antialias=True)
        self.world_y_axis = gl.GLLinePlotItem(pos=np.array([[0, 0, 0], [0, world_axis_length, 0]]), color=(0, 1, 0, 1), width=2, antialias=True)
        self.world_z_axis = gl.GLLinePlotItem(pos=np.array([[0, 0, 0], [0, 0, world_axis_length]]), color=(0, 0, 1, 1), width=2, antialias=True)
        self.view.addItem(self.world_x_axis)
        self.view.addItem(self.world_y_axis)
        self.view.addItem(self.world_z_axis)
        
        # 원기둥에 고정된 축 추가
        body_axis_length = 2
        self.body_x_axis = gl.GLLinePlotItem(pos=np.array([[0, 0, 0], [body_axis_length, 0, 0]]), color=(1, 0.5, 0.5, 1), width=2, antialias=True)
        self.body_y_axis = gl.GLLinePlotItem(pos=np.array([[0, 0, 0], [0, body_axis_length, 0]]), color=(0.5, 1, 0.5, 1), width=2, antialias=True)
        self.body_z_axis = gl.GLLinePlotItem(pos=np.array([[0, 0, 0], [0, 0, body_axis_length]]), color=(0.5, 0.5, 1, 1), width=2, antialias=True)
        self.view.addItem(self.body_x_axis)
        self.view.addItem(self.body_y_axis)
        self.view.addItem(self.body_z_axis)

    def update_attitude(self, roll, pitch, yaw):
        """실제 데이터를 사용하여 3D 모델을 회전시킵니다."""
        self.cylinder.resetTransform()
        self.cylinder.rotate(roll, 1, 0, 0)
        self.cylinder.rotate(pitch, 0, 1, 0)
        self.cylinder.rotate(yaw, 0, 0, 1)
        
        self.body_x_axis.resetTransform()
        self.body_y_axis.resetTransform()
        self.body_z_axis.resetTransform()
        self.body_x_axis.rotate(roll, 1, 0, 0)
        self.body_x_axis.rotate(pitch, 0, 1, 0)
        self.body_x_axis.rotate(yaw, 0, 0, 1)
        self.body_y_axis.rotate(roll, 1, 0, 0)
        self.body_y_axis.rotate(pitch, 0, 1, 0)
        self.body_y_axis.rotate(yaw, 0, 0, 1)
        self.body_z_axis.rotate(roll, 1, 0, 0)
        self.body_z_axis.rotate(pitch, 0, 1, 0)
        self.body_z_axis.rotate(yaw, 0, 0, 1)

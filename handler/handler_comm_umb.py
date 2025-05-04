from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtCore import QIODevice, QObject, QTimer
from PyQt5.QtWidgets import QMessageBox
import json
from datetime import datetime

from utils.data_types import DataVehicle, parse_csv_to_vehicle


class HandlerCommUMB(QObject):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.serial_port = QSerialPort()
        self.serial_connected = False
        self.buffer = b""
        
        # 데이터 수신 속도 측정을 위한 변수들
        self.packet_count = 0
        self.last_packet_count = 0
        self.last_update_time = datetime.now()
        
        # 1초마다 속도 업데이트하는 타이머
        self.rate_timer = QTimer()
        self.rate_timer.timeout.connect(self._update_rate)
        self.rate_timer.start(1000)  # 1초 간격

    def connect_serial(self, port_name, baudrate):
        """
        시리얼 포트 연결/해제 처리
        """
        if not self.serial_connected:
            self.serial_port.setPortName(port_name)
            self.serial_port.setBaudRate(baudrate)
            self.serial_port.setDataBits(QSerialPort.Data8)
            self.serial_port.setParity(QSerialPort.NoParity)
            self.serial_port.setStopBits(QSerialPort.OneStop)
            self.serial_port.setFlowControl(QSerialPort.NoFlowControl)

            if self.serial_port.open(QIODevice.ReadWrite):
                self.serial_connected = True
                self.controller.ui.PB_UMB_SER_CONN.setText("Connected!")
                self.serial_port.readyRead.connect(self._handle_ready_read)
                # 연결 시 카운터 초기화
                self.packet_count = 0
                self.last_packet_count = 0
                self.last_update_time = datetime.now()
                return True
            else:
                QMessageBox.critical(self.controller.ui, "Error", "Failed to open UMB serial port.")
                return False
        else:
            # 이미 연결된 경우 -> 해제
            self.serial_connected = False
            self.serial_port.close()
            self.controller.ui.PB_UMB_SER_CONN.setText("Connect\nSerial")
            return False

    def _update_rate(self):
        """
        1초마다 호출되어 데이터 수신 속도를 계산하고 UI에 표시
        """
        if not self.serial_connected:
            self.controller.ui.LB_UMB_RATE.setText("0.0 Hz")
            return
            
        current_time = datetime.now()
        time_diff = (current_time - self.last_update_time).total_seconds()
        
        if time_diff > 0:
            rate = (self.packet_count - self.last_packet_count) / time_diff
            self.controller.ui.LB_UMB_RATE.setText(f"{rate:.1f} Hz")
            
            # 속도 계산 후 카운터 리셋 (오버플로우 방지)
            self.last_packet_count = 0
            self.packet_count = 0
            self.last_update_time = current_time

    def _handle_ready_read(self):
        """
        시리얼 버퍼에 데이터가 있을 때 호출됨
        """
        while self.serial_port.canReadLine():
            try:
                line = self.serial_port.readLine().data().decode("utf-8").strip()
                if not line:
                    continue

                if ',' in line:
                    self._handle_csv_packet(line)
                else:
                    self._append_debug_message(line)
            except Exception as e:
                self._append_debug_message(f"[UMB] Error while reading serial data: {e}")

    def _handle_csv_packet(self, line):
        """
        CSV 형식: 예) 1.23,2.34,3.45,...,13.37
        """
        try:
            data = parse_csv_to_vehicle(line, source="UMB")
            self.packet_count += 1
            self.controller.on_umb_data_received(data)
        except ValueError as e:
            self._append_debug_message(f"[UMB] CSV parse error:{line}")
        except Exception as e:
            self._append_debug_message(f"[UMB] Unexpected CSV error: {e}")

    def _append_debug_message(self, line):
        """
        TE_GCS_DEBUG에 한 줄씩 출력 (최대 100줄 유지)
        """
        # 컨트롤러의 메서드를 호출
        self.controller._append_debug_message(line)

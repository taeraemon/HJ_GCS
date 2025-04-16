from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtCore import QIODevice, QObject, pyqtSignal

class PipeSerial(QObject):
    packet_received = pyqtSignal(bytes)

    def __init__(self, port_name="COM1", baudrate=115200):
        super().__init__()
        self.serial = QSerialPort()
        self.serial.setPortName(port_name)
        self.serial.setBaudRate(baudrate)
        self.serial.readyRead.connect(self._read_data)
        self.buffer = b""

    def open(self):
        return self.serial.open(QIODevice.ReadWrite)

    def close(self):
        self.serial.close()

    def _read_data(self):
        self.buffer += self.serial.readAll().data()
        while b'\n' in self.buffer:  # 패킷 종료 조건 예시
            packet, self.buffer = self.buffer.split(b'\n', 1)
            self.packet_received.emit(packet)

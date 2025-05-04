from dataclasses import dataclass
from datetime import datetime
from typing import List, Tuple

@dataclass
class DataGSE:
    timestamp: datetime
    roll  : float
    pitch : float
    yaw   : float

@dataclass
class DataVehicle:
    nav_roll: float
    nav_pitch: float
    nav_yaw: float

@dataclass
class ReceivedPacket:
    data: DataVehicle
    timestamp: datetime
    source: str

def parse_csv_to_vehicle(line: str, source: str) -> ReceivedPacket:
    try:
        parts = line.strip().split(',')
        if len(parts) < 3:
            raise ValueError("Incomplete CSV data")

        values = list(map(float, parts[:3]))

        data_vehicle = DataVehicle(
            nav_roll=values[0],
            nav_pitch=values[1],
            nav_yaw=values[2]
        )

        return ReceivedPacket(
            data=data_vehicle,
            timestamp=datetime.now(),
            source=source
        )
    except Exception as e:
        raise ValueError(f"CSV parsing failed: {e}")



    # # ===== 시간 관련 =====
    # timestamp: datetime
    # boot_time: float            # 부팅 후 경과 시간 (초)
    # mode_time: float            # 현재 모드 시작 후 경과 시간 (초)

    # # ===== 센서 데이터 =====
    # # 압력 센서 (10채널)
    # pressures: List[float]      # [p1, p2, ..., p10] (Pa)
    
    # # 온도 센서 (10채널)
    # temperatures: List[float]   # [t1, t2, ..., t10] (°C)
    
    # # 밸브 상태 (10채널)
    # valve_states: List[bool]    # [v1, v2, ..., v10] (True: 개방, False: 폐쇄)
    
    # # 전기 데이터
    # voltage: float             # 시스템 전압 (V)
    # current: float             # 시스템 전류 (A)

    # # ===== 시스템 상태 =====
    # state: int                 # 현재 상태 (정수 코드)
    # sequence: int              # 현재 준비된 시퀀스 번호
    # error_code: int            # 고장 코드 (비트 플래그)

    # # ===== 시스템 모니터링 =====
    # cpu_usage: float          # CPU 사용률 (%)
    # memory_usage: float       # 메모리 사용률 (%)
    # sd_total_size: float      # SD 카드 총 용량 (MB)
    # sd_used_size: float       # SD 카드 사용량 (MB)

    # # ===== IMU 데이터 =====
    # # 3축 가속도 (m/s²)
    # accel_x: float
    # accel_y: float
    # accel_z: float
    
    # # 3축 각속도 (rad/s)
    # gyro_x: float
    # gyro_y: float
    # gyro_z: float

    # # ===== GPS 데이터 =====
    # # GPS 생 측정치 (위도, 경도, 고도)
    # gps_lat: float            # 위도 (deg)
    # gps_lon: float            # 경도 (deg)
    # gps_alt: float            # 고도 (m)
    
    # gps_satellites: int       # 가시 위성 수
    # gps_time: datetime        # GPS 시간
    # gps_constellation: str    # GPS Constellation 정보
    
    # # GPS 수신기 상태
    # gps_fix_type: int         # 0: No fix, 1: Dead reckoning, 2: 2D, 3: 3D, 4: GNSS+DR
    # gps_fix_quality: int      # 0: Invalid, 1: GPS fix, 2: DGPS fix, 3: PPS fix, 4: RTK fixed, 5: RTK float
    # gps_hdop: float          # 수평 정확도 (Horizontal Dilution of Precision)
    # gps_vdop: float          # 수직 정확도 (Vertical Dilution of Precision)
    # gps_pdop: float          # 위치 정확도 (Position Dilution of Precision)
    # gps_ground_speed: float  # 지상 속도 (m/s)
    # gps_course: float        # 진행 방향 (deg, 0~360)
    # # ===== 항법 데이터 =====
    # # 3축 자세 (deg)
    # nav_roll: float
    # nav_pitch: float
    # nav_yaw: float
    
    # # 4축 쿼터니언
    # nav_qw: float
    # nav_qx: float
    # nav_qy: float
    # nav_qz: float
    
    # # 3축 위치 (m)
    # nav_x: float
    # nav_y: float
    # nav_z: float
    
    # # 3축 속도 (m/s)
    # nav_vx: float
    # nav_vy: float
    # nav_vz: float


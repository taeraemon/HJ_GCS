from dataclasses import dataclass
from datetime import datetime

@dataclass
class DataUMB:
    timestamp: datetime
    roll  : float
    pitch : float
    yaw   : float

@dataclass
class DataTLM:
    timestamp: datetime
    roll  : float
    pitch : float
    yaw   : float

@dataclass
class DataGSE:
    timestamp: datetime
    roll  : float
    pitch : float
    yaw   : float

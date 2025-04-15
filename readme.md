프로그램 이름은 VFCommandCenter

발사체 지상 관제 및 제어, 지상 설비 관제 및 제어, 발사체 비행 관제 및 제어를 위한 통합 소프트웨어


윈도우에서 pyqt 및 qt designer를 통해 개발 예정.
따라서 VFCommandCenter.ui이 생길 예정.

VFCommandCenter.py에서 main 함수를 관리



데이터가 들어오면 실시간으로 그래프 그림 및 수치 표시
다만 데이터가 들어오면 업데이트 하는 형태의 로직은 데이터가 들어오지 않으면 화면이 업데이트 되지 않으니,
데이터가 들어오면 그걸 담아두는 클래스와, 그걸 기반으로 화면을 업데이트하는 비동기 느낌의 형태로 로직을 구현

ui는 세 종류의 탭이 있을 예정 (GNC, PR, MISSION), 따라서 하나의 탭을 선택하면 해당 탭에 존재하면 객체만 업데이트 하는 방식이 효율적이지 않을까 생각.

명령을 보내는 부분 따로.

또한 발사체, 지상 설비, 텔레메트리 모듈과는 시리얼 포트로 연결될 수도, ip로 연결될 수도 있음. 따라서 둘 다 대응 가능한 클래스를 만들기.





VFCommandCenter/
│
├── VFCommandCenter.py
│
├── ui/
│   └── VFCommandCenter.ui   # Qt Designer로 만든 UI 파일
│
├── core/
│   └── core_controller.py   # 모든 핸들러를 연결하고 전체 제어
│
├── handler/
│   ├── handler_ui.py        # UI 핸들링 클래스
│   ├── handler_plot.py      # 실시간 플롯 처리
│   ├── handler_log.py       # 로그 저장 처리
│   ├── handler_comm_gse.py  # GSE 관련 핸들링
│   ├── handler_comm_umb.py  # Umbilical 관련 핸들링
│   └── handler_comm_tlm.py  # Telemetry 관련 핸들링
│
├── pipe/
│   ├── pipe_serial.py       # 저수준 시리얼 read/write
│   └── pipe_network.py      # 저수준 IP 통신 read/write
│
├── utils/
│   └── data_types.py        # 데이터 파싱/변환 유틸
│
├── resource/
│   └── icon.png             # UI에서 쓸 아이콘들
│
└── models/                  # (필요 시) ML 모델 or 구조화된 데이터 저장


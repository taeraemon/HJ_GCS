# 🚀 HJ GCS (지상관제시스템)

## 소개
로켓/비행체 모니터링용 지상관제시스템. PyQt5 기반으로 시리얼 통신으로 데이터 수신 및 시각화함.

## 설치방법
pyenv+venv 기반으로 진행됨. (파이썬 버전 3.10으로 테스트됨)

```bash
pip install PyQt5 pyqtgraph PyOpenGL PyOpenGL_accelerate
```

## 실행방법
```bash
python VFCommandCenter.py
```

## 사용법

### 1. 통신 연결
- **Umbilical**: Refresh 버튼 클릭 → 포트 선택 → 속도 설정(기본 115200) → Connect 클릭
- **Telemetry/GSE**: 위와 동일한 방법으로 연결함

### 2. 데이터 확인
- Umbilical/Telemetry 버튼 클릭으로 데이터 소스 선택함
- LOG 버튼 눌러서 데이터 기록 시작/중지함 (logs 폴더에 저장됨)
- Tab 1: 센서 데이터 그래프, Tab 2: 3D 자세 시각화 볼 수 있음
- 화면 오른쪽에 상태정보, 하단 오른쪽에 디버그 메시지 표시됨

## 주의사항
- 프로그램 시작 전 장비 연결 상태 확인하기
- 로깅 중 강제종료 하지 말기

## TODO
- 웹 지도에 비행체 위치 표시 기능



&nbsp;
<details>
<summary>📦 패키지 설치 세부 과정</summary>

```
pip list

Package Version
------- -------
pip     24.0

pip install pyqt5

Package   Version
--------- -------
pip       24.0
PyQt5     5.15.11
PyQt5-Qt5 5.15.2
PyQt5_sip 12.17.0

pip install pyqtgraph

Package   Version
--------- -------
numpy     2.2.5
pip       24.0
PyQt5     5.15.11
PyQt5-Qt5 5.15.2
PyQt5_sip 12.17.0
pyqtgraph 0.13.7

pip install PyOpenGL

Package   Version
--------- -------
numpy     2.2.5
pip       24.0
PyOpenGL  3.1.9
PyQt5     5.15.11
PyQt5-Qt5 5.15.2
PyQt5_sip 12.17.0
pyqtgraph 0.13.7

pip install PyOpenGL_accelerate

Package             Version
------------------- -------
numpy               2.2.5
pip                 24.0
PyOpenGL            3.1.9
PyOpenGL-accelerate 3.1.9
PyQt5               5.15.11
PyQt5-Qt5           5.15.2
PyQt5_sip           12.17.0
pyqtgraph           0.13.7
```
</details>
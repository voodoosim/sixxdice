# sixxdice
project/
│
├── main.py              # 봇 실행 및 초기화
├── .env                 # 민감한 정보 (TOKEN 등) 관리
├── config/
│   ├── settings.py      # 환경설정 및 상수
│
├── handlers/
│   ├── admin_handler.py # 관리자 핸들러
│   ├── user_handler.py  # 사용자 핸들러
│   ├── game_handler.py  # 게임 핸들러
│
├── managers/
│   ├── database.py      # 데이터베이스 클래스
│   ├── user_manager.py  # 사용자 관련 기능
│   ├── admin_manager.py # 관리자 관련 기능
│   ├── game_manager.py  # 게임 관련 기능
│
├── db/
│   ├── db_pool.py       # 비동기 DB 연결 풀
│
├── utils/
│   ├── helpers.py       # 공통 유틸리티 함수
│
└── requirements.txt     # 필요한 패키지

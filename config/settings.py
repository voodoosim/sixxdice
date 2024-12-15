import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# 텔레그램 봇 설정
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ALLOWED_GROUP_CHAT_ID = int(os.getenv("ALLOWED_GROUP_CHAT_ID", "0"))
OTHER_GROUP_CHAT_ID = int(os.getenv("OTHER_GROUP_CHAT_ID", "0"))
REQUIRED_CHANNEL_ID = int(os.getenv("REQUIRED_CHANNEL_ID", "0"))

# 관리자 ID
ADMIN_IDS = [40912620, 7224325221, 6500697563]

# 필수 값 검증
if not TOKEN:
    raise ValueError("봇 토큰이 설정되지 않았습니다. .env 파일을 확인하세요.")
if not ALLOWED_GROUP_CHAT_ID or not REQUIRED_CHANNEL_ID:
    raise ValueError("그룹 및 채널 ID가 설정되지 않았습니다.")

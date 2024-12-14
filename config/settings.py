import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# 텔레그램 봇 토큰
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# 관리자 ID 리스트
ADMIN_IDS = [40912620, 7224325221, 6500697563, 7480970367]

# 그룹/채널 설정
ALLOWED_GROUP_CHAT_ID = -1001931591623
OTHER_GROUP_CHAT_ID = -1002081646431
REQUIRED_CHANNEL_ID = -1001129730806


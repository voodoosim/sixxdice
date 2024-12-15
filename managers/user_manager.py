from datetime import datetime
from telegram import Update
from config.settings import REQUIRED_CHANNEL_ID


class UserManager:
    def __init__(self, database):
        self.db = database

    async def handle_check_in(self, update: Update, context):
        """출석 체크 처리"""
        user_id = update.effective_user.id
        today = datetime.now().strftime("%Y-%m-%d")
        user_data = await self.db.get_user_data(user_id)

        if user_data and user_data["last_check_in_date"] == today:
            await update.message.reply_text("오늘 이미 출석체크를 완료했습니다.")
            return

        # 포인트 지급
        if not user_data:
            user_data = {"id": user_id, "hearts": 100, "check_in_count": 1, "last_check_in_date": today}
        else:
            user_data["hearts"] += 100
            user_data["check_in_count"] += 1
            user_data["last_check_in_date"] = today

        await self.db.save_user_data(user_data)
        await update.message.reply_text(f"출석체크 완료! +100포인트 지급되었습니다.")

    async def verify_group(self, update: Update, context, allowed_groups):
        """허용된 그룹에서만 동작 확인"""
        chat_id = update.effective_chat.id
        if chat_id not in allowed_groups:
            await update.message.reply_text("이 그룹에서는 명령어를 사용할 수 없습니다.")

from telegram import Update


class UserManager:
    def __init__(self, database):
        self.db = database

    async def handle_check_in(self, update: Update, context):
        # 사용자 체크인 처리
        user_id = update.message.from_user.id
        user_data = await self.db.get_user_data(user_id)
        if not user_data:
            user_data = {
                "id": user_id,
                "hearts": 100,  # 기본 포인트
                "check_in_count": 0
            }
            await self.db.save_user_data(user_data)

        user_data["hearts"] += 100
        user_data["check_in_count"] += 1
        await self.db.save_user_data(user_data)
        await update.message.reply_text(f"출석 완료! 포인트 +100")

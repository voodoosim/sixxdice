from telegram.ext import MessageHandler, filters
from managers.user_manager import UserManager
from config.settings import ALLOWED_GROUP_CHAT_ID, OTHER_GROUP_CHAT_ID


async def setup_user_handlers(application):
    """사용자 명령어 핸들러를 설정합니다."""
    user_manager = UserManager(application.bot_data["db"])
    application.bot_data["user_manager"] = user_manager

    # 출석 체크 핸들러
    application.add_handler(MessageHandler(
        filters.Regex(r'^\.출첵$'),
        lambda update, context: user_manager.handle_check_in(update, context)
    ))

    # 그룹 검증 핸들러 (허용된 그룹인지 확인)
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        lambda update, context: user_manager.verify_group(update, context, [ALLOWED_GROUP_CHAT_ID, OTHER_GROUP_CHAT_ID])
    ))

    print("사용자 핸들러가 설정되었습니다.")

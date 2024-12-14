from telegram.ext import MessageHandler, filters
from managers.user_manager import UserManager


async def setup_user_handlers(application):
    user_manager = UserManager(application.bot_data["db"])
    application.bot_data["user_manager"] = user_manager

    # 출첵 명령어
    application.add_handler(MessageHandler(
        filters.Regex(r'^\.출첵$'),
        lambda update, context: user_manager.handle_check_in(update, context)
    ))

    # 포인트 전송
    application.add_handler(MessageHandler(
        filters.Regex(r'^\.주기\s+@\w+\s+\d+$') | filters.REPLY,
        lambda update, context: user_manager.give_points(update, context)
    ))
    print("사용자 핸들러가 설정되었습니다.")

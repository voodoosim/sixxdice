from .user_handler import setup_user_handlers
from .admin_handler import setup_admin_handlers
from .game_handler import setup_game_handlers


async def setup_handlers(application):
    """모든 핸들러를 설정합니다."""
    await setup_user_handlers(application)
    await setup_admin_handlers(application)
    await setup_game_handlers(application)
    print("모든 핸들러가 설정되었습니다.")

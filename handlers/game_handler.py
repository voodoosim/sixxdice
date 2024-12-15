from telegram.ext import Application
from managers.game_manager import GameManager


async def setup_game_handlers(application: Application):
    """게임 핸들러를 설정합니다."""
    game_manager = GameManager(application.bot_data["db"])
    application.bot_data["game_manager"] = game_manager

    # 90초 간격으로 주사위 송출
    job_queue = application.job_queue
    job_queue.run_repeating(
        callback=lambda context: asyncio.create_task(game_manager.start_game(context)),
        interval=90,  # 90초마다 실행
        first=10  # 봇 시작 후 10초 뒤 첫 실행
    )

    print("게임 핸들러가 설정되었습니다.")

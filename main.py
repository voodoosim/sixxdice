import asyncio
from telegram.ext import Application
from config.settings import TOKEN
from handlers import setup_handlers
from managers.database import Database


async def main():
    # 애플리케이션 초기화
    application = Application.builder().token(TOKEN).build()

    # 데이터베이스 초기화
    db = Database()
    await db.init_db()
    application.bot_data["db"] = db

    # 핸들러 등록
    await setup_handlers(application)

    # 봇 시작
    await application.initialize()
    await application.start()
    await application.bot.delete_webhook(drop_pending_updates=True)
    print("봇이 실행 중입니다...")

    try:
        await asyncio.Event().wait()  # 무한 대기
    finally:
        await application.stop()
        await db.close_all()


if __name__ == "__main__":
    asyncio.run(main())

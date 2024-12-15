from telegram import Update
from telegram.ext import ContextTypes
import asyncio
from config.settings import ALLOWED_GROUP_CHAT_ID


class GameManager:
    """게임 관리 클래스"""

    def __init__(self, database):
        self.db = database
        self.is_game_active = False

    async def start_game(self, context: ContextTypes.DEFAULT_TYPE):
        """90초마다 주사위를 송출"""
        if self.is_game_active:
            return

        self.is_game_active = True
        chat_id = ALLOWED_GROUP_CHAT_ID

        try:
            # 주사위 3개 송출
            dice_results = []
            await context.bot.send_message(chat_id=chat_id, text="🎲 주사위를 던집니다!")
            for _ in range(3):
                dice_message = await context.bot.send_dice(chat_id=chat_id)
                dice_results.append(dice_message.dice.value)
                await asyncio.sleep(0.5)

            # 결과 처리
            total = sum(dice_results)
            result = "짝수" if total % 2 == 0 else "홀수"
            await context.bot.send_message(chat_id=chat_id, text=f"🎲 결과: {dice_results} (총합: {total})\n✨ 결과: {result}")
        finally:
            self.is_game_active = False

from aiogram import Dispatcher
from db_connection import get_session
from models import Novel
from view import View


class Controller():
    def __init__(self, dp: Dispatcher, view: View):
        self.dp = dp
        self.view = view

    async def send_message_to_user(self, user_id: int, message: str):
        await self.dp.bot.send_message(user_id, message)
        await self.view.send_message(message)

    async def test(self):
        session = get_session()
        result = await session.query(Novel).filter(
            Novel.english_name == self.title).first()
        await self.view.show_novel(result)

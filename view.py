from typing import List
# from aiogram import types
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from models import Novel


class View():

    async def show_novel(self, novel: List[Novel]):
        for elem in Novel:
            await self.dp.bot.send_message(Novel.id, f"{Novel.original_name}")

    # async def start(self, message: types.Message):
    #     keyboard = InlineKeyboardMarkup(row_width=1)
    #     button = InlineKeyboardButton("Нажми меня",
    #                                   callback_data='button_pressed')
    #     keyboard.add(button)
    #     await message.answer("Привет! Я бот. Нажми на кнопку:",
    #                          reply_markup=keyboard)

    # async def button_pressed(self, callback_query: types.CallbackQuery):
    #     await callback_query.answer("Кнопка нажата!")
    #     await callback_query.message.answer("Спасибо за нажатие кнопки!")

    # async def send_file(self, message: types.Message):
    #     with open('path/to/file', 'rb') as file:
    #         await message.answer_document(file)

    # async def send_message(self, message: types.Message):
    #     user_id = message.from_user.id
    #     await self.controller.send_message_to_user(
    #         user_id,
    #         "Привет, я отправил тебе сообщение в личку!")

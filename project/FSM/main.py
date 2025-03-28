import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


class Form(StatesGroup):
    name = State()
    age = State()


@dp.message(Command('start'))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer("Как вас зовут?")


@dp.message(Form.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.age)
    await message.answer(
        f"Приятно познакомиться, {message.text}! Сколько вам лет?")


@dp.message(Form.age)
async def process_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введите число!")
        return

    data = await state.get_data()
    await message.answer(
        f"Спасибо, что заполнили анкету!\n"
        f"Имя: {data["name"]}\n"
        f"Возраст {message.text}"
    )
    await state.clear()


if __name__ == '__main__':
    dp.run_polling(bot)

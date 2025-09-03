from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    name = State()
    age = State()


async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer("Как вас зовут?")


async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.age)
    await message.answer(
        f"Приятно познакомиться, {message.text}! Сколько вам лет?")


async def process_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введите число!")
        return

    data = await state.get_data()
    await message.answer(
        f"Спасибо, что заполнили анкету!\n"
        f"Имя: {data['name']}\n"
        f"Возраст: {message.text}"
    )
    await state.clear()

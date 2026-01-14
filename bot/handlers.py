from datetime import date

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from core.manager import CoreManager
from loguru import logger


router = Router()
core_manager = CoreManager()


@router.message(Command("start"))
async def cmd_start(message: Message):
    """Handle /start command"""
    await message.answer(
        "Привет! Я бот для управления домашними делами. "
        "Я помогу вам с планированием питания, расписанием уборки, "
        "напоминаниями о важных событиях и финансами."
    )


@router.message(Command("help"))
async def cmd_help(message: Message):
    """Handle /help command"""
    help_text = (
        "Доступные команды:\n"
        "/start - Начать работу с ботом\n"
        "/help - Показать это сообщение\n"
        "/dates - Просмотр всех памятных дат\n"
        "/adddate - Добавить новую памятную дату (формат: /adddate имя дата(ГГГГ-ММ-ДД) категория [описание])\n"
        "/upcoming - Просмотр предстоящих дат\n"
        "/housework - Просмотр всех домашних дел\n"
        "/addtask - Добавить новую задачу (формат: /addtask название [длительность] [частота])\n"
        "/duetasks - Просмотр задач, которые нужно выполнить сегодня\n"
        "/completetask - Отметить задачу как выполненную (формат: /completetask ID)\n"
        "/finance - Финансовое планирование\n"
        "/timetable - Поздравления, памятные даты"
    )
    await message.answer(help_text)


@router.message(Command("dates"))
async def cmd_dates(message: Message):
    """Handle /dates command - show all memorable dates"""
    try:
        logger.info(f"Пользователь {message.from_user.id} запросил список памятных дат")
        timetable_manager = core_manager.get_timetable_manager()
        dates = timetable_manager.get_all_memorable_dates()

        if not dates:
            await message.answer("Пока нет сохраненных памятных дат.")
            return

        response = "Все памятные даты:\n\n"
        for date_record in dates:
            date_id, name, date_str, description, category, created_at = date_record
            age_or_anniversary = timetable_manager.calculate_age_or_anniversary(date_id)

            response += f"<b>{name}</b>\n"
            response += f"Дата: {date_str}\n"
            response += f"Категория: {category or 'Не указана'}\n"
            if description:
                response += f"Описание: {description}\n"
            if age_or_anniversary is not None:
                if category and category.lower() == 'birthday':
                    response += f"Возраст: {age_or_anniversary} лет\n"
                elif category and category.lower() == 'anniversary':
                    response += f"Юбилей: {age_or_anniversary} лет\n"
            response += "\n"

        await message.answer(response)
        logger.info(f"Список памятных дат отправлен пользователю {message.from_user.id}")
    except Exception as e:
        logger.error(f"Ошибка при обработке команды /dates: {e}")
        await message.answer("Произошла ошибка при получении списка памятных дат.")


@router.message(Command("adddate"))
async def cmd_add_date(message: Message):
    """Handle /adddate command - add a new memorable date"""
    # Пример: /adddate Иван Иванов 1990-05-15 День рождения ДР
    try:
        logger.info(f"Пользователь {message.from_user.id} запросил добавление памятной даты")
        args = message.text.split()[1:]  # Пропускаем команду

        if len(args) < 3:
            await message.answer(
                "Использование: /adddate <имя> <дата(ГГГГ-ММ-ДД)> <категория> [описание]\n"
                "Пример: /adddate Иван Иванов 1990-05-15 birthday День рождения\n"
                "Доступные категории: birthday, anniversary, holiday, other"
            )
            return

        # Собираем имя (может состоять из нескольких слов)
        date_idx = None
        for i, arg in enumerate(args):
            try:
                # Пробуем распознать дату
                date.fromisoformat(arg)
                date_idx = i
                break
            except ValueError:
                continue

        if date_idx is None:
            await message.answer("Пожалуйста, укажите дату в формате ГГГГ-ММ-ДД")
            return

        name = " ".join(args[:date_idx])
        date_str = args[date_idx]

        # Категория обязательна
        category = args[date_idx + 1] if len(args) > date_idx + 1 else None

        # Описание (если указано)
        description = " ".join(args[date_idx + 2:]) if len(args) > date_idx + 2 else None

        # Проверяем формат даты
        try:
            date.fromisoformat(date_str)
        except ValueError:
            await message.answer("Дата должна быть в формате ГГГГ-ММ-ДД")
            return

        # Добавляем дату
        timetable_manager = core_manager.get_timetable_manager()
        date_id = timetable_manager.add_memorable_date(name, date_str, description, category)

        await message.answer(f"Памятная дата '{name}' добавлена с ID {date_id}")
        logger.info(f"Пользователь {message.from_user.id} добавил памятную дату '{name}' с ID {date_id}")

    except Exception as e:
        logger.error(f"Ошибка при обработке команды /adddate: {e}")
        await message.answer(f"Ошибка при добавлении даты: {str(e)}")


@router.message(Command("upcoming"))
async def cmd_upcoming(message: Message):
    """Handle /upcoming command - show upcoming memorable dates"""
    try:
        logger.info(f"Пользователь {message.from_user.id} запросил список предстоящих дат")
        timetable_manager = core_manager.get_timetable_manager()
        upcoming_dates = timetable_manager.get_upcoming_dates(7)  # На 7 дней вперед

        if not upcoming_dates:
            await message.answer("В ближайшие 7 дней нет памятных дат.")
            return

        response = "Предстоящие памятные даты (в ближайшие 7 дней):\n\n"
        for date_record in upcoming_dates:
            date_id, name, date_str, description, category = date_record
            age_or_anniversary = timetable_manager.calculate_age_or_anniversary(date_id)

            response += f"<b>{name}</b>\n"
            response += f"Дата: {date_str}\n"
            response += f"Категория: {category or 'Не указана'}\n"
            if description:
                response += f"Описание: {description}\n"
            if age_or_anniversary is not None:
                if category and category.lower() == 'birthday':
                    response += f"Будет {age_or_anniversary} лет\n"
                elif category and category.lower() == 'anniversary':
                    response += f"Будет {age_or_anniversary} лет со дня события\n"
            response += "\n"

        await message.answer(response)
        logger.info(f"Список предстоящих дат отправлен пользователю {message.from_user.id}")
    except Exception as e:
        logger.error(f"Ошибка при обработке команды /upcoming: {e}")
        await message.answer("Произошла ошибка при получении списка предстоящих дат.")


@router.message(Command("housework"))
async def cmd_housework(message: Message):
    """Handle /housework command - show all housework tasks"""
    try:
        logger.info(f"Пользователь {message.from_user.id} запросил список домашних дел")
        housework_manager = core_manager.get_housework_manager()
        tasks = housework_manager.get_all_housework_tasks()

        if not tasks:
            await message.answer("Пока нет запланированных домашних дел.")
            return

        response = "Все домашние дела:\n\n"
        for task in tasks:
            task_id, name, duration, frequency, last_completed, created_at = task

            response += f"<b>{name}</b>\n"
            response += f"ID: {task_id}\n"
            if duration:
                response += f"Продолжительность: {duration} мин\n"
            if frequency:
                response += f"Частота: {frequency}\n"
            if last_completed:
                response += f"Последнее выполнение: {last_completed}\n"
            else:
                response += "Последнее выполнение: Не выполнено\n"
            response += "\n"

        await message.answer(response)
        logger.info(f"Список домашних дел отправлен пользователю {message.from_user.id}")
    except Exception as e:
        logger.error(f"Ошибка при обработке команды /housework: {e}")
        await message.answer("Произошла ошибка при получении списка домашних дел.")


@router.message(Command("addtask"))
async def cmd_add_task(message: Message):
    """Handle /addtask command - add a new housework task"""
    try:
        logger.info(f"Пользователь {message.from_user.id} запросил добавление задачи")
        args = message.text.split()[1:]  # Пропускаем команду

        if len(args) < 1:
            await message.answer(
                "Использование: /addtask <название> [длительность(мин)] [частота(daily/weekly/monthly/yearly)]\n"
                "Пример: /addtask Протереть пыль 30 weekly"
            )
            return

        name = " ".join(args[:len(args)-2]) if len(args) > 2 else args[0]
        duration = int(args[-2]) if len(args) > 1 and args[-2].isdigit() else None
        frequency = args[-1] if len(args) > 0 and args[-1] in ['daily', 'weekly', 'monthly', 'yearly'] else None

        # Добавляем задачу
        housework_manager = core_manager.get_housework_manager()
        task_id = housework_manager.add_housework_task(name, duration, frequency)

        await message.answer(f"Задача '{name}' добавлена с ID {task_id}")
        logger.info(f"Пользователь {message.from_user.id} добавил задачу '{name}' с ID {task_id}")

    except Exception as e:
        logger.error(f"Ошибка при обработке команды /addtask: {e}")
        await message.answer(f"Ошибка при добавлении задачи: {str(e)}")


@router.message(Command("duetasks"))
async def cmd_due_tasks(message: Message):
    """Handle /duetasks command - show tasks that are due today"""
    try:
        logger.info(f"Пользователь {message.from_user.id} запросил список задач на сегодня")
        housework_manager = core_manager.get_housework_manager()
        due_tasks = housework_manager.get_due_tasks()

        if not due_tasks:
            await message.answer("Сегодня нет задач, которые нужно выполнить.")
            return

        response = "Задачи, которые нужно выполнить сегодня:\n\n"
        for task in due_tasks:
            task_id, name, duration, frequency, last_completed, created_at = task

            response += f"<b>{name}</b>\n"
            response += f"ID: {task_id}\n"
            if duration:
                response += f"Продолжительность: {duration} мин\n"
            if frequency:
                response += f"Частота: {frequency}\n"
            if last_completed:
                response += f"Последнее выполнение: {last_completed}\n"
            else:
                response += f"Последнее выполнение: Никогда\n"
            response += "\n"

        await message.answer(response)
        logger.info(f"Список задач на сегодня отправлен пользователю {message.from_user.id}")
    except Exception as e:
        logger.error(f"Ошибка при обработке команды /duetasks: {e}")
        await message.answer("Произошла ошибка при получении списка задач на сегодня.")


@router.message(Command("completetask"))
async def cmd_complete_task(message: Message):
    """Handle /completetask command - mark a task as completed"""
    try:
        logger.info(f"Пользователь {message.from_user.id} запросил выполнение задачи")
        args = message.text.split()[1:]  # Пропускаем команду

        if len(args) != 1:
            await message.answer(
                "Использование: /completetask <ID задачи>\n"
                "Пример: /completetask 1"
            )
            return

        task_id = int(args[0])

        # Проверяем, существует ли задача
        housework_manager = core_manager.get_housework_manager()
        task = housework_manager.get_housework_task_by_id(task_id)

        if not task:
            await message.answer(f"Задача с ID {task_id} не найдена.")
            logger.warning(f"Пользователь {message.from_user.id} запросил несуществующую задачу с ID {task_id}")
            return

        # Отмечаем задачу как выполненную
        housework_manager.mark_task_completed(task_id)

        task_id, name, duration, frequency, last_completed, created_at = task
        await message.answer(f"Задача '{name}' отмечена как выполненная.")
        logger.info(f"Пользователь {message.from_user.id} отметил задачу {task_id} как выполненную")

    except ValueError:
        await message.answer("ID задачи должен быть числом.")
        logger.warning(f"Пользователь {message.from_user.id} ввел некорректный ID задачи")
    except Exception as e:
        logger.error(f"Ошибка при обработке команды /completetask: {e}")
        await message.answer(f"Ошибка при выполнении задачи: {str(e)}")


def setup_handlers(dp):
    """Register all handlers with dispatcher"""
    dp.include_router(router)

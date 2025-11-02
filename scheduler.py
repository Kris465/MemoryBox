from datetime import datetime
from loguru import logger
from parser import UniversityParser
from bot import send_schedule_to_telegram


class ScheduleChecker:
    def __init__(self):
        self.last_check = None

    async def check_schedule_daily(self):
        """Ежедневная проверка расписания (для совместимости)"""
        logger.info("🔔 Выполняем ежедневную проверку расписания")

        try:
            async with UniversityParser(headless=True,
                                        use_saved_session=True) as parser:
                result = await parser.get_schedule_for_date()
                message = self.format_telegram_message(result)
                await send_schedule_to_telegram(message)

                self.last_check = datetime.now()
                logger.info("Проверка расписания завершена")

        except Exception as e:
            logger.error(f"Ошибка при проверке расписания: {e}")
            error_msg = f"Ошибка при получении расписания: {str(e)}"
            await send_schedule_to_telegram(error_msg)

    def format_telegram_message(self, schedule_result: dict) -> str:
        """Форматируем сообщение для Telegram"""
        if not schedule_result.get('success'):
            error_msg = schedule_result.get('error', 'Неизвестная ошибка')
            return f"*Не удалось получить расписание*\n\nОшибка: {error_msg}"

        schedule_data = schedule_result.get('schedule', {})
        date = schedule_result.get('date', 'Неизвестная дата')

        try:
            date_obj = datetime.strptime(date, '%Y-%m-%d')
            formatted_date = date_obj.strftime('%d.%m.%Y')
            weekday = self._get_weekday_russian(date_obj.weekday())
            date_display = f"{formatted_date} ({weekday})"
        except:
            date_display = date

        message = f"*Расписание на {date_display}*\n"
        message += f"{schedule_data.get('group_info', 'Группа не определена')}\n\n"

        if not schedule_data.get('has_classes', False):
            if schedule_data.get('next_class_date'):
                message += "*Занятий нет*\n"
                message += f"Ближайшее занятие — {schedule_data['next_class_date']}"
            else:
                message += "*Занятий нет*"
        else:
            message += "*Сегодня есть занятия:*\n\n"

            classes = schedule_data.get('classes', [])
            for i, class_info in enumerate(classes, 1):
                message += f"*{i}. {class_info.get('subject', 'Дисциплина')}*"

                if class_info.get('time'):
                    message += f"{class_info['time']}\n"
                if class_info.get('room'):
                    message += f"{class_info['room']}\n"
                if class_info.get('teacher'):
                    message += f"{class_info['teacher']}\n"

                message += "\n"

        message += f"\n_Обновлено: {datetime.now().strftime('%H:%M')}_"
        return message

    def _get_weekday_russian(self, weekday: int) -> str:
        """Получаем день недели на русском"""
        days = ['Понедельник', 'Вторник',
                'Среда', 'Четверг', 'Пятница',
                'Суббота', 'Воскресенье']
        return days[weekday]

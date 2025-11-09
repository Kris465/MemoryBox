import json
import os
from datetime import datetime
from typing import Dict, List, Optional
from loguru import logger


class ScheduleJsonTools:
    """Класс для работы с JSON файлом расписания"""

    def __init__(self, json_filename: str = 'calendar_events.json'):
        self.json_filename = json_filename

    def save_events_to_json(self, events_data: List[Dict]) -> bool:
        """Сохраняет события в JSON файл"""
        try:
            with open(self.json_filename, 'w', encoding='utf-8') as f:
                json.dump(events_data, f, ensure_ascii=False, indent=2)
            logger.info(f"Данные сохранены в {self.json_filename}")
            return True
        except Exception as e:
            logger.error(f"Ошибка сохранения в JSON: {e}")
            return False

    def load_events_from_json(self) -> Optional[List[Dict]]:
        """Загружает события из JSON файла"""
        try:
            if not os.path.exists(self.json_filename):
                return None

            with open(self.json_filename, 'r', encoding='utf-8') as f:
                events_data = json.load(f)
            logger.info(f"Загружено {len(events_data)} событий из {self.json_filename}")
            return events_data
        except Exception as e:
            logger.error(f"Ошибка загрузки из JSON: {e}")
            return None

    def get_schedule_for_date(self, target_date: datetime) -> Dict:
        """
        Получает расписание на указанную дату из JSON файла
        """
        date_str = target_date.strftime('%Y-%m-%d')

        events_data = self.load_events_from_json()
        if events_data is None:
            return {
                'success': False,
                'error': 'Файл с расписанием не найден',
                'date': date_str,
                'schedule': {'has_classes': False}
            }

        day_events = [event for event in events_data if event.get('date') == date_str]

        schedule_data = {
            'has_classes': len(day_events) > 0,
            'classes': [],
            'group_info': 'БМЗ-25'
        }

        for event in day_events:
            parsed = event.get('parsed', {})
            class_info = {
                'subject': parsed.get('subject', 'Неизвестно'),
                'time': parsed.get('time', ''),
                'room': parsed.get('room', ''),
                'teacher': parsed.get('teacher', ''),
                'type': parsed.get('type', ''),
                'raw_text': event.get('text', '')
            }
            schedule_data['classes'].append(class_info)

        # Ищем ближайшее занятие если сегодня нет занятий
        if not schedule_data['has_classes']:
            next_class = self._find_next_class(events_data, target_date)
            if next_class:
                schedule_data['next_class_date'] = next_class

        return {
            'success': True,
            'date': date_str,
            'schedule': schedule_data
        }

    def _find_next_class(self, events_data: List[Dict],
                         from_date: datetime) -> Optional[str]:
        """Находит ближайшее занятие после указанной даты"""
        try:
            future_events = []

            for event in events_data:
                event_date = event.get('date')
                if event_date:
                    event_dt = datetime.strptime(event_date, '%Y-%m-%d')
                    if event_dt >= from_date:
                        future_events.append((event_dt, event))

            if future_events:
                future_events.sort(key=lambda x: x[0])
                next_event_date = future_events[0][0]
                return next_event_date.strftime('%d.%m.%Y')

            return None

        except Exception as e:
            logger.warning(f"Ошибка поиска ближайшего занятия: {e}")
            return None

    def file_exists(self) -> bool:
        """Проверяет существование файла с расписанием"""
        return os.path.exists(self.json_filename)

import os
from loguru import logger
from tqdm import tqdm
import threading
import queue

from models import GenerationRequest
from document_processor import DocumentProcessor
from vector_db import VectorDatabase
from llm_client import LLMClient


class SearchAssistant:
    def __init__(self):
        logger.info("Инициализация Search Assistant")

        # Инициализация компонентов
        self.document_processor = DocumentProcessor()
        self.vector_db = VectorDatabase()
        
        # Инициализация LLM клиента
        try:
            self.llm_client = LLMClient()
            logger.info("✅ LLM клиент инициализирован")
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации LLM клиента: {e}")
            self.llm_client = None

        # Очередь для статуса генерации
        self.status_queue = queue.Queue()
        self.generation_active = False
        self.last_activity_time = time.time()

        # Пути
        self.standards_path = "./standards"
        self.sources_path = "./sources"

        self._check_directories()

    def _check_directories(self):
        """Проверка существования необходимых директорий"""
        os.makedirs(self.standards_path, exist_ok=True)
        os.makedirs(self.sources_path, exist_ok=True)

        standard_files = os.listdir(self.standards_path)
        if not standard_files:
            logger.warning("⚠️  В папке standards нет файлов!")
            logger.info("📝 Положите файл assignment.txt в папку standards")
        else:
            logger.info(f"📋 Найден стандарт: {standard_files[0]}")

        source_files = os.listdir(self.sources_path)
        if not source_files:
            logger.warning("📚 В папке sources нет файлов!")
            logger.info("📖 Добавьте PDF/DOCX файлы в папку sources")
        else:
            logger.info(f"📖 Найдено источников: {len(source_files)}")

    def _status_monitor(self):
        """Монитор статуса для показа прогресса"""
        inactivity_threshold = 45  # секунд
        warning_sent = False
        
        while self.generation_active:
            try:
                message = self.status_queue.get(timeout=10)
                if message:
                    logger.info(f"🔄 {message}")
                    self.last_activity_time = time.time()
                    warning_sent = False
                    
                    # Выводим сообщение в консоль с временной меткой
                    current_time = time.strftime("%H:%M:%S")
                    print(f"[{current_time}] {message}")
                    
            except queue.Empty:
                # Проверяем не зависла ли генерация
                time_since_last_activity = time.time() - self.last_activity_time
                
                if time_since_last_activity > inactivity_threshold and not warning_sent:
                    logger.warning(f"⚠️  Нет активности {time_since_last_activity:.0f} секунд...")
                    print(f"⏰ ВНИМАНИЕ: Генерация не активна {time_since_last_activity:.0f} секунд")
                    print("💡 Возможно модель 'думает' или произошло зависание")
                    warning_sent = True
                
                continue

    def _show_progress(self, message):
        """Отправка сообщения о прогрессе"""
        if self.generation_active:
            self.status_queue.put(message)
            self.last_activity_time = time.time()

    def generate_work(self, assignment, topic, context):
        """Генерация работы на основе задания и контекста"""
        if not self.llm_client:
            raise RuntimeError("LLM клиент не инициализирован")

        logger.info("🎨 Начинаю генерацию работы...")
        print("\n" + "="*60)
        print("🚀 ЗАПУСК ГЕНЕРАЦИИ РАБОТЫ")
        print("="*60)

        # Создаем запрос на генерацию
        request = GenerationRequest(
            assignment=assignment,
            topic=topic,
            context=context,
            style="academic"
        )

        # Запускаем монитор статуса
        self.generation_active = True
        self.last_activity_time = time.time()
        
        status_thread = threading.Thread(target=self._status_monitor, daemon=True)
        status_thread.start()

        try:
            # Выводим стартовую информацию
            self._show_progress("🎯 Подготовка к генерации...")
            time.sleep(1)  # Даем время для отображения
            
            result = self.llm_client.generate_text(
                request, 
                status_callback=self._show_progress
            )

            self.generation_active = False
            status_thread.join(timeout=2)

            return result

        except Exception as e:
            self.generation_active = False
            status_thread.join(timeout=2)
            logger.error(f"❌ Ошибка генерации: {e}")
            self._show_progress(f"❌ Ошибка: {str(e)}")
            raise e

    def read_assignment(self):
        """Чтение задания из файла в standards"""
        try:
            standard_files = os.listdir(self.standards_path)
            if not standard_files:
                raise FileNotFoundError("Нет файлов в папке standards")

            # Берем первый файл
            assignment_file = os.path.join(self.standards_path,
                                           standard_files[0])
            logger.info(f"📖 Чтение задания: {assignment_file}")

            # Определяем тип файла и читаем
            if assignment_file.lower().endswith('.txt'):
                with open(assignment_file, 'r', encoding='utf-8') as f:
                    assignment_text = f.read()
            elif assignment_file.lower().endswith('.docx'):
                assignment_text = self.document_processor.extract_text_from_docx(assignment_file)
            else:
                raise ValueError(f"Неподдерживаемый формат файла: {assignment_file}")

            logger.info(f"✅ Задание прочитано ({len(assignment_text)} символов)")
            return assignment_text

        except Exception as e:
            logger.error(f"❌ Ошибка чтения задания: {e}")
            return None

    def load_sources(self):
        """Загрузка всех источников в векторную БД"""
        logger.info("🔄 Начало загрузки источников в базу данных")

        source_files = os.listdir(self.sources_path)
        if not source_files:
            logger.warning("📚 Нет файлов для загрузки")
            return False

        total_loaded = 0

        with tqdm(total=len(source_files), desc="📥 Загрузка источников") as pbar:
            for filename in source_files:
                file_path = os.path.join(self.sources_path, filename)

                try:
                    # Загружаем документ в векторную БД
                    chunks_count = self.vector_db.add_document(file_path)
                    if chunks_count > 0:
                        total_loaded += chunks_count
                        logger.debug(f"✅ Загружен {filename}: {chunks_count} фрагментов")
                    else:
                        logger.warning(f"⚠️  Не удалось загрузить {filename}")

                except Exception as e:
                    logger.error(f"❌ Ошибка загрузки {filename}: {e}")

                pbar.update(1)

        logger.info(f"✅ Загружено {total_loaded} фрагментов из {len(source_files)} файлов")
        return total_loaded > 0

    def search_relevant_content(self, topic):
        """Поиск релевантного контента по теме"""
        logger.info(f"🔍 Поиск по теме: {topic}")

        try:
            search_result = self.vector_db.search(topic, n_results=10)

            if not search_result.chunks:
                logger.warning("⚠️  По запросу ничего не найдено")
                return ""

            # Формируем контекст из найденных фрагментов
            context_parts = []
            for i, chunk in enumerate(search_result.chunks[:5]):  # Берем топ-5
                context_parts.append(f"[Источник: {chunk.source}]")
                context_parts.append(chunk.text)
                context_parts.append("---")

            context = "\n".join(context_parts)
            logger.info(f"✅ Найдено {len(search_result.chunks)} релевантных фрагментов")

            return context

        except Exception as e:
            logger.error(f"❌ Ошибка поиска: {e}")
            return ""

    def run(self):
        """Основной цикл работы ассистента"""
        logger.info("🚀 Запуск основного цикла")

        # 1. Читаем задание
        assignment = self.read_assignment()
        if not assignment:
            logger.error("❌ Не удалось прочитать задание!")
            return

        print("\n" + "="*50)
        print("📋 ЗАДАНИЕ:")
        print("="*50)
        print(assignment[:500] + "..." if len(assignment) > 500 else assignment)
        print("="*50)

        # 2. Извлекаем тему из задания
        topic = self._extract_topic_from_assignment(assignment)
        if not topic:
            # Если не удалось извлечь тему, запрашиваем у пользователя
            print("\n🎯 Введите тему работы:")
            topic = input("> ").strip()

        if not topic:
            logger.error("❌ Тема не может быть пустой!")
            return

        logger.info(f"🎯 Тема работы: {topic}")

        # 3. Загружаем источники
        if not self.load_sources():
            logger.warning("База источников пуста, генерация без контекста")

        # 4. Ищем релевантный контент
        context = self.search_relevant_content(topic)

        # 5. Генерируем работу
        logger.info("🎨 Начинаю генерацию работы...")
        result = self.generate_work(assignment, topic, context)

        # 6. Сохраняем и показываем результат
        output_file = "result.md"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result)

        print("\n" + "="*50)
        print("РЕЗУЛЬТАТ:")
        print("="*50)
        print(result)
        print("=" * 50)
        logger.info(f"Результат сохранен в {output_file}")

    def _extract_topic_from_assignment(self, assignment: str) -> str:
        """Улучшенное извлечение темы из текста задания"""
        try:
            lines = assignment.split('\n')
            
            # Ищем различные варианты обозначения темы
            topic_keywords = ['тема:', 'topic:', 'название:', 'title:']
            
            for line in lines:
                line_lower = line.lower().strip()
                for keyword in topic_keywords:
                    if line_lower.startswith(keyword):
                        topic = line[len(keyword):].strip(' :')
                        if topic and len(topic) > 5:  # Минимальная длина темы
                            logger.info(f"📖 Извлечена тема из задания: {topic}")
                            return topic

            # Если не нашли по ключевым словам, берем первую содержательную строку
            for line in lines:
                line = line.strip()
                if (line and 
                    len(line) > 10 and 
                    not line.startswith(('#', '=', '-', '*'))):
                    logger.info(f"📖 Использую первую строку как тему: {line}")
                    return line[:100]  # Ограничиваем длину

            return ""

        except Exception as e:
            logger.error(f"Ошибка извлечения темы: {e}")
            return ""

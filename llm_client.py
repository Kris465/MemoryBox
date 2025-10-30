from typing import Optional, Callable
from loguru import logger
import ollama
from tqdm import tqdm
import time

from models import GenerationRequest


class LLMClient:
    def __init__(self, default_model: str = "mistral:latest"):
        logger.info("Инициализация LLM Client")
        
        # Принудительно создаем клиента с явным указанием хоста
        self.client = ollama.Client(host='http://127.0.0.1:11434', timeout=30)
        
        try:
            # Простая проверка
            self.client.list()
            logger.info("✅ Подключение к Ollama установлено")
        except Exception as e:
            logger.error(f"❌ Ошибка подключения к Ollama: {e}")
            raise ConnectionError(f"Ollama недоступен: {e}")

    def _check_ollama_availability(self) -> bool:
        """Проверка доступности Ollama"""
        try:
            self.client.list()
            return True
        except Exception:
            return False

    def _get_available_models(self) -> dict:
        """Получение списка доступных моделей"""
        try:
            models = self.client.list()
            return {model['name']: model for model in models['models']}
        except Exception as e:
            logger.error(f"Ошибка получения списка моделей: {e}")
            return {}

    def generate_text(
        self,
        request: GenerationRequest,
        model: Optional[str] = None,
        status_callback: Optional[Callable] = None
    ) -> str:
        """Генерация текста с визуальным прогрессом"""
        
        target_model = model or self.default_model
        
        if status_callback:
            status_callback("🔧 Подготовка промпта...")

        # Создаем промпт
        prompt = self._create_prompt(request)
        
        logger.info(f"🚀 Запуск генерации с моделью {target_model}")
        logger.info(f"📝 Длина промпта: {len(prompt)} символов")
        
        if status_callback:
            status_callback("🎯 Начинаю генерацию...")

        try:
            # Инициализируем прогресс-бар
            self._start_progress_monitor()
            
            # Засекаем время начала
            start_time = time.time()
            
            # Генерация с обработкой потока
            response = self._generate_with_progress(target_model, prompt, status_callback)
            
            # Вычисляем время выполнения
            generation_time = time.time() - start_time
            
            # Завершаем прогресс-бар
            self._stop_progress_monitor()
            
            result = response.strip()
            
            logger.info(f"✅ Генерация завершена за {generation_time:.1f} сек")
            logger.info(f"📄 Результат: {len(result)} символов, {len(result.split())} слов")
            
            if status_callback:
                status_callback(f"✅ Генерация завершена! ({len(result)} символов)")
            
            return result
            
        except Exception as e:
            self._stop_progress_monitor()
            logger.error(f"❌ Ошибка генерации: {e}")
            if status_callback:
                status_callback("❌ Ошибка генерации!")
            raise e

    def _generate_with_progress(self, model: str, prompt: str, status_callback: Optional[Callable] = None):
        """Генерация с отслеживанием прогресса"""
        full_response = ""
        last_update = time.time()
        generated_tokens = 0
        
        # Используем stream для отслеживания прогресса
        stream = self.client.generate(
            model=model,
            prompt=prompt,
            options={
                'num_predict': 8000,
                'temperature': 0.7
            },
            stream=True
        )
        
        for chunk in stream:
            if 'response' in chunk:
                full_response += chunk['response']
                generated_tokens += 1
                
                # Обновляем прогресс каждые 0.5 секунды или каждые 10 токенов
                current_time = time.time()
                if current_time - last_update > 0.5 or generated_tokens % 10 == 0:
                    if status_callback:
                        status_callback(f"📝 Генерирую... ({generated_tokens} токенов, {len(full_response)} символов)")
                    
                    # Обновляем прогресс-бар
                    self._update_progress(len(full_response), generated_tokens)
                    last_update = current_time
                
                # Проверяем не зависла ли генерация (если прошло больше 30 секунд без новых токенов)
                if current_time - last_update > 30:
                    logger.warning("⚠️  Возможное зависание генерации...")
                    if status_callback:
                        status_callback("⚠️  Проверка генерации...")
        
        return full_response

    def _start_progress_monitor(self):
        """Запуск мониторинга прогресса в терминале"""
        self.progress_bar = tqdm(
            total=8000,  # Максимальное количество токенов
            desc="🎯 Генерация",
            unit="токен",
            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]"
        )
        self.start_time = time.time()

    def _update_progress(self, chars_count: int, tokens_count: int):
        """Обновление прогресс-бара"""
        if self.progress_bar:
            # Обновляем количество токенов
            self.progress_bar.n = tokens_count
            
            # Добавляем дополнительную информацию
            self.progress_bar.set_postfix(
                chars=f"{chars_count} симв.",
                refresh=True
            )
            
            # Обновляем отображение
            self.progress_bar.refresh()

    def _stop_progress_monitor(self):
        """Остановка мониторинга прогресса"""
        if self.progress_bar:
            self.progress_bar.close()
            self.progress_bar = None

    def _create_prompt(self, request: GenerationRequest) -> str:
        """Создание промпта для генерации"""
        prompt = f"""
        # ЗАДАНИЕ ДЛЯ НАПИСАНИЯ НАУЧНОЙ РАБОТЫ

        ## ОСНОВНОЕ ЗАДАНИЕ:
        {request.assignment}

        ## ТЕМА РАБОТЫ:
        {request.topic}

        ## ИСХОДНЫЕ МАТЕРИАЛЫ И КОНТЕКСТ:
        {request.context if request.context else "Дополнительные источники не предоставлены"}

        ## ТРЕБОВАНИЯ К РАБОТЕ:
        - Стиль: {request.style}
        - Структура: введение, основная часть, заключение
        - Объем: развернутый, подробный анализ
        - Использовать академический язык
        - Ссылаться на предоставленные источники

        Напиши полноценную научную работу на основе задания и материалов.
                """
        return prompt.strip()

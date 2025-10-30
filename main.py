"""
Research Assistant - основной модуль запуска
Автоматизированное написание научных работ
"""

import sys
from loguru import logger
from assistant import SearchAssistant


def setup_logging():
    """Настройка логирования"""
    logger.remove()

    logger.add(
        "logs/app.log",
        rotation="10 MB",
        retention="30 days",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}"
    )

    # Логи в консоль с цветами
    logger.add(
        sys.stderr,
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="INFO",
        colorize=True
    )


def check_environment():
    """Проверка необходимого окружения"""
    logger.info("🔍 Проверка окружения...")
    
    try:
        import requests
        # Пробуем только 127.0.0.1:11434
        host = "http://127.0.0.1:11434"
        logger.info(f"🔄 Проверка подключения к {host}")
        
        response = requests.get(f"{host}/api/tags", timeout=10)
        
        if response.status_code == 200:
            logger.info(f"✅ Ollama доступен на {host}")
            
            # Покажем доступные модели
            try:
                models = response.json()
                model_names = [model['name'] for model in models.get('models', [])]
                if model_names:
                    logger.info(f"📋 Доступные модели: {', '.join(model_names)}")
                else:
                    logger.warning("⚠️  Нет доступных моделей")
            except:
                logger.info("📋 Модели: информация недоступна")
                
            return True
        else:
            logger.error(f"❌ Ollama вернул ошибку: {response.status_code}")
            logger.info(f"💡 Ответ сервера: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        logger.error(f"❌ Не удалось подключиться к Ollama")
        logger.info("💡 Убедитесь что Ollama запущен: ollama serve")
        return False
    except Exception as e:
        logger.error(f"❌ Ошибка проверки окружения: {e}")
        return False


def print_banner():
    """Печать баннера приложения"""
    banner = """
    ╔══════════════════════════════════════════╗
    ║           RESEARCH ASSISTANT             ║
    ║    Автоматизированное написание работ    ║
    ╚══════════════════════════════════════════╝
    """
    print(banner)


def main():
    """Основная функция запуска"""
    try:
        # Настройка
        setup_logging()
        print_banner()
        
        # Проверка окружения
        if not check_environment():
            logger.error("Проверка окружения не пройдена")
            sys.exit(1)
        
        # Создание и запуск ассистента
        logger.info("Запуск Research Assistant...")
        assistant = SearchAssistant()
        
        # Проверяем, что LLM клиент инициализирован
        if assistant.llm_client is None:
            logger.error("❌ LLM клиент не инициализирован!")
            logger.info("💡 Проверьте:")
            logger.info("   - Запущен ли Ollama: ollama serve")
            logger.info("   - Установлена ли модель: ollama pull mistral")
            logger.info("   - Доступен ли localhost:11434")
            sys.exit(1)
        
        print("\n✅ Все системы готовы к работе!")
        print("📊 Статус компонентов:")
        print(f"   - LLM клиент: ✅ готов")
        print(f"   - Векторная БД: ✅ готов") 
        print(f"   - Обработчик документов: ✅ готов")
        print("\n🎯 Запускаю основной цикл...\n")
        
        # Запуск основного цикла
        assistant.run()
        
    except KeyboardInterrupt:
        logger.info("Работа прервана пользователем")
        print("\n⏹️  Генерация прервана пользователем")
    except Exception as e:
        logger.error(f"Критическая ошибка: {e}")
        print(f"\n❌ Критическая ошибка: {e}")
        sys.exit(1)
    finally:
        logger.info("Работа завершена")
        print("\n👋 Работа завершена")


if __name__ == "__main__":
    main()

# Currency Converter

Конвертер валют на Django.

## Установка и запуск

### 1. Создать виртуальное окружение

```bash
python -m venv .venv
```

### 2. Активировать виртуальное окружение

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Создать миграции

```bash
python manage.py makemigrations
```

### 5. Применить миграции

```bash
python manage.py migrate
```

### 6. Запустить сервер разработки

```bash
python manage.py runserver
```

После этого проект будет доступен по адресу: http://127.0.0.1:8000/

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Подключение к базе данных
engine = create_engine('...')
Base = declarative_base()

# Определение модели данных


class User(Base):
    __tablename__ = 'workers'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(30))
    name = Column(String(12))
    email = Column(String(25))

# Создание сессии для выполнения запросов


Session = sessionmaker(bind=engine)
session = Session()

# Выполнение запроса на получение списка пользователей
users = session.query(User).all()

# Вывод списка пользователей
for user in users:
    print(user.id, user.nickname, user.name, user.email)

# Закрытие сессии
session.close()

import json
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv
import models


class Repository():

    def __init__(self):
        self.__session = self.set_session()

    @property
    def session(self):
        return self.__session

    def set_session(self):
        load_dotenv(find_dotenv())
        user = os.environ.get('user')
        password = os.environ.get('password')
        host = os.environ.get('host')
        database = os.environ.get('database')
        engine = create_engine(
            f'mysql+mysqlconnector://{user}:{password}@{host}/{database}',
            )
        Session = sessionmaker(bind=engine)
        return Session

    def find(self, query):
        tables = [models.Novel, models.Author, models.Genre]
        for table in tables:
            result = self.session.query(table).filter(
                                                table.name == query).first()
        if result:
            self.show_table(table.__tablename__)
            return True
        return False

    def save_objects(self, *args):
        for obj in args:
            table_class = type(obj)
            if hasattr(models, table_class.__name__):
                self.session.add(obj)
            else:
                raise ValueError(f"Object {obj} is not a valid database table")
        self.session.commit()

    def show_table(self, name):
        result = self.session.query(name).all()
        for row in result:
            print(row.__dict__.format())

    def write(name, data, language=None):
        with open(f"{name}.json", "w", encoding='UTF-8') as file:
            if language == 'chi':
                json.dump(data, file, ensure_ascii=False)
            else:
                json.dump(data, file)

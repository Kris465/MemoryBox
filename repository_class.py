import json
import os
import pprint
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv
import models


class Repository():

    def __init__(self):
        self._session = self.create_session()

    @property
    def session(self):
        return self._session()

    def create_session(self):
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
        tables = [models.Novel,
                  models.Chapters,
                  models.Projects,
                  models.Workers,
                  models.Status]
        for table in tables:
            result = self.session.query(table).filter(
                                                table.english_name == query
                                                ).first()
            if result:
                self.show_table(table.__tablename__)
                self.session.close()
                return True
        return False

    # def save_objects(self, *args):
    #     for obj in args:
    #         table_class = type(obj)
    #         if hasattr(models, table_class.__name__):
    #             self.session.add(obj)
    #         else:
    #             raise ValueError(f"Object {obj} is not a valid database table")
    #     self.session.commit()
    #     self.session.close()
    # def save_objects(self, *args):
    #     for obj in args:
    #         table_class = type(obj)
    #         if hasattr(models, f'{table_class}'):
    #             table_class_table = getattr(models, f"{table_class.name}Table")
    #             table_obj = table_class_table(**obj.__dict__)
    #             self.session.add(table_obj)
    #         else:
    #             raise ValueError(f"Object {obj} is not a valid database table")
    #     self.session.commit()
    #     self.session.close()

    # def save_objects(self, *args):
    #     for obj in args:
    #         table_class = type(obj)
    #         if hasattr(models, f'{table_class.__name__}'):
    #             table_class_table = getattr(models, f"{table_class.__name__}Table")
    #             table_obj = table_class_table(**obj.__dict__)
    #             self.session.add(table_obj)
    #         else:
    #             raise ValueError(f"Object {obj} is not a valid database table")
    #     self.session.commit()
    #     self.session.close()
    
    def save_objects(self, *args):
        for obj in args:
            table_class = type(obj)
            table_name = table_class.__name__
            table_class_table = getattr(models, f"{table_name}Table", None)
            if table_class_table:
                obj_dict = obj.__dict__
                table_obj = table_class_table(**obj_dict)
                self.session.add(table_obj)
            else:
                raise ValueError(f"Object {obj} is not a valid database table")
        self.session.commit()
        self.session.close()


    # def save_objects(self, *args):
    #     for obj in args:
    #         table_class = type(obj)
    #         if hasattr(models, f'{table_class.__name__}'):
    #             table_class_table = getattr(models, f"{table_class.__name__}")
    #             table_obj = table_class_table(**obj.__dict__)
    #             self.session.add(table_obj)
    #         else:
    #             raise ValueError(f"Object {obj} is not a valid database table")
    #     self.session.commit()
    #     self.session.close()

    def show_table(self, name):
        tables = [models.Chapters,
                  models.Projects,
                  models.Status,
                  models.Workers,
                  models.Novel]
        for table in tables:
            result = self.session.query(table).all()
        for row in result:
            print(row.__dict__)
        self.session.close()

    def write(name, data, language=None):
        with open(f"{name}.json", "w", encoding='UTF-8') as file:
            if language == 'chi':
                json.dump(data, file, ensure_ascii=False)
            else:
                json.dump(data, file)

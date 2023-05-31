import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv

from models import Novel


class Repository():

    def __init__(self) -> None:
        self.session = self.get_session()

    def get_session(self):
        load_dotenv(find_dotenv())
        user = os.environ.get('user')
        password = os.environ.get('password')
        host = os.environ.get('host')
        database = os.environ.get('database')
        engine = create_engine(
            f'mysql+mysqlconnector://{user}:{password}@{host}/{database}',
            )
        Session = sessionmaker(bind=engine)
        return Session()

    def find(self, title):
        result = self.session.query(Novel).filter(
            Novel.english_name == title).all()
        if len(result) == 1:
            return True
        else:
            return False

    def language(self, title):
        # return Chinese
        # return English
        pass

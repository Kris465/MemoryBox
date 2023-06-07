import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv


def get_session():
    load_dotenv(find_dotenv())
    user = os.environ.get('user')
    password = os.environ.get('password')
    host = os.environ.get('host')
    database = os.environ.get('database')
    engine = create_engine(
        f'mysql+mysqlconnector://{user}:{password}@{host}/{database}',
        pool_recycle=3600
        )
    Session = sessionmaker(bind=engine)
    return Session()

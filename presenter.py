from db_connection import get_session
from models import Workers


class Presenter:
    def __init__(self, view):
        self.view = view

    def add_worker(self, nickname,
                   name,
                   phone=None,
                   email=None,
                   vk=None,
                   birthday=None,
                   comment="editor"):
        worker = Workers(nickname=nickname,
                         name=name,
                         phone=phone,
                         email=email,
                         vk=vk,
                         birthday=birthday,
                         comment=comment)
        session = get_session()
        session.add(worker)
        session.commit()
        session.close()

        self.view.show_message('Пользователь добавлен')

Для создания записей в несколько таблиц за раз вам нужно использовать транзакции. Транзакции позволяют выполнить несколько операций в одной сессии, и если хотя бы одна из операций не выполнится успешно, то все изменения будут отменены.

Пример кода для создания проекта, новеллы и главы:

python
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Создаем сессию подключения к БД
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Создаем статус проекта
    status = Status(status='in progress')
    session.add(status)

    # Создаем исполнителя проекта
    worker = Workers(nickname='john', name='John Doe')
    session.add(worker)

    # Создаем проект и связываем его со статусом и исполнителем
    project = Projects(comment='New project', status=status, worker=worker)
    session.add(project)

    # Создаем новеллу и связываем ее с проектом
    novel = Novel(russian_name='Новелла', project=project)
    session.add(novel)

    # Создаем главы и связываем их с новеллой
    chapter1 = Chapters(ordinal_number=1, link='chapter1.html', novel=novel)
    session.add(chapter1)
    chapter2 = Chapters(ordinal_number=2, link='chapter2.html', novel=novel)
    session.add(chapter2)

    # Завершаем транзакцию
    session.commit()

except IntegrityError:
    # Если произошла ошибка, откатываем изменения
    session.rollback()

finally:
    # Закрываем сессию
    session.close()


В этом примере мы создаем статус проекта, исполнителя проекта, проект, новеллу и две главы, связывая их друг с другом. Если произойдет ошибка при выполнении какой-либо операции, то все изменения будут отменены.
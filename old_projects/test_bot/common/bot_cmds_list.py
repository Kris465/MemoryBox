from aiogram.types import BotCommand

private = [
    BotCommand(command='start', description='Начать диалог с ботом'),
    BotCommand(command='topics', description='Посмотреть темы'),
    BotCommand(command='rating', description='Посмотреть общий рейтинг'),
    BotCommand(command='results', description='Посмотреть свои результаты'),
    BotCommand(command='joke', description='Расскажи анекдот')
]

class Parser:
    '''
    Работает ТОЛЬКО с 1 главой
    1. Учитывает защиту сайтов
    2. Расчленяет и извлекает текст
    '''

    def __init__(self, url) -> None:
        self.url = url
        self.text = ''

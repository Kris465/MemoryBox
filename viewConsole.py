import os


class ViewConsole:
    def __init__(self):
        pass
    @staticmethod
    def display_info(field):
        os.system("CLS")
        print("-" * 50)
        [print(i) for i in field.field]
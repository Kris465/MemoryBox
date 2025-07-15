from tools.file_manager import read_from_json


class Links_manager:
    def __init__(self):
        self.projects = read_from_json("novels.json")

    def logic(self):
        pass
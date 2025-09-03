import os
import json


class Reader:
    def __init__(self) -> None:
        self.all_tasks = {}
        self.folder_path = 'tasks/'

    def collect_all_tasks(self):
        index = 0
        for file_name in os.listdir(self.folder_path):
            if file_name.endswith('.json'):
                file_path = os.path.join(self.folder_path, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    if "tasks" in data:
                        needed_dict = data["tasks"][0]
                        for task in needed_dict.values():
                            self.all_tasks[index] = task
                            index += 1
        return self.all_tasks

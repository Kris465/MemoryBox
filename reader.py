import json
import os


class Reader:
    def __init__(self) -> None:
        self.all_tasks = {}
        self.folder_path = 'tasks/'

    def collect_all_tasks(self):
        for file_name in os.listdir(self.folder_path):
            if file_name.endswith('.json'):
                file_path = os.path.join(self.folder_path, file_name)
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    if "tasks" in data:
                        inner_dict = data["tasks"][0]
                        self.all_tasks.update(inner_dict)
        return self.all_tasks

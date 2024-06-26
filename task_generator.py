import random


class TaskGenerator:
    def __init__(self, number, tasks) -> None:
        self.number = number
        self.tasks = tasks

    def choose_tasks(self):
        all_keys = list(self.tasks.keys())
        random_keys = random.sample(all_keys, self.number)

        new_dict = {key: self.tasks[key] for key in random_keys}
        return new_dict

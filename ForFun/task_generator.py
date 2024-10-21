import itertools
import random


class TaskGenerator:
    def __init__(self, number, tasks) -> None:
        self.number = number
        self.tasks = tasks

    def choose_tasks(self):
        shuffled_keys = list(self.tasks.keys())
        random.shuffle(shuffled_keys)
        self.tasks = {key: self.tasks[key] for key in shuffled_keys}

        new_dict = dict(itertools.islice(self.tasks.items(), self.number))

        return new_dict

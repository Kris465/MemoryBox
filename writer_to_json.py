import json
from novel import Novel

class File_operator:

    def __init__(self, novel):
        with open(f"projects/{Novel.title}.json", "w", encoding="UTF-8") as file:
            json.dump(data, file)

    def __init__(self, file):
        pass

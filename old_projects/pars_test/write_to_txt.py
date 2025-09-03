import json

with open('female.json', 'r') as json_file:
    data = json.load(json_file)

with open('output.txt', 'w') as txt_file:
    for key, value in data.items():
        txt_file.write(f"{key}: {value}\n")

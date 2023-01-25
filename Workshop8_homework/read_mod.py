"""
Reading ssv module
"""

import csv

def reader(argument):
    with open("busses.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")

        if argument[0] == "0":
            answer = [row for row in file_reader]
        elif argument[0] == "1":
            real_arg = int(argument[1:])
            answer = [row for row in file_reader if real_arg]
        elif argument[0] == "2":
            real_arg = int(argument[1:])
            answer = [row[(real_arg) - 1] for row in file_reader]
        else:answer = "AAAAAAAAAAA"
    
    return answer
    
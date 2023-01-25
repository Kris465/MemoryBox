"""
Writing csv module
"""

import csv

with open("busses.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(["Имя", "Класс", "Возраст"])
    file_writer.writerow(["Женя", "3", "10"])
    file_writer.writerow(["Саша", "5", "12"])
    file_writer.writerow(["Маша", "11", "18"])
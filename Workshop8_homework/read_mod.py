"""
Reading ssv module
"""

import csv

def reader(use_choice):
    with open("busses.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        count = 0
        rows = [row for row in file_reader if count == 0]
    
    return rows
    
"""
Reading ssv module
"""

import csv

def take():
    lst = []
    with open("vars.csv", encoding='utf-8') as r_file:
        lst = csv.reader(r_file, delimiter = ",")
        #lst = [row for row in read_object]

    return lst
    
"""
Writing csv module
"""

def put(use_lst):

    with open("vars.csv", mode="w", newline='', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file)
        for elem in range(len(use_lst)):
            file_writer.writerow(use_lst[elem])

"""
Writing csv module
"""

import csv

def writer(use_lst):

    with open("busses.csv", mode="w", newline='', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file)
        for elem in range(len(use_lst)):
            file_writer.writerow(use_lst[elem])
        
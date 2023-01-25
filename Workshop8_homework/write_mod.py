"""
Writing csv module
"""

import csv

def writer(use_lst):
    with open("busses.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")

        if use_lst[-1] == 0:
            file_writer.writerow(use_lst[:-1])
        elif use_lst[-1] == 1:
            file_writer.writerow(use_lst[:-2])
        else: print("AAAAAAAAAAA")
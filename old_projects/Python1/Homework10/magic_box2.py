"""
Reading ssv module
"""

import csv

def take():
    lst = []
    with open("vars.csv", encoding='utf-8') as f:
        lst = list(f.readlines()[0].split(","))[0:]
        #lst = [row for row in read_object]

    return lst
    
"""
Writing csv module
"""

def put(use_lst):

    with open("vars.csv", mode="w", encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')

        for elem in use_lst:
            elem = ",".join([ch for ch in elem if ch != "[" or ch != "]"])
            print(elem)

        writer.writerow(use_lst)
        

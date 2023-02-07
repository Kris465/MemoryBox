"""
This module writes everything in app. 
It writes: date, time, type of action, input data, results, exceptions
"""

import logging

logging.basicConfig(
        level=logging.DEBUG,
        filename="my_log.log",
        filemode="w",
        format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s - %(message)s",
        datefmt='%d-%m-%Y %H:%M:%S')

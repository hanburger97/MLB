import numpy as np
import pandas as pd



def readData(fileName):
    """
    Trying to read in raw data of game log formats it into a list separated by commas
    :param fileName:
    :return:
    """
    fs = open(fileName, "r")
    string_stream = fs.read()
    list_of_values = string_stream.split()
    if 0 == len(list_of_values):
        raise Exception("List of values parsed incorrectly by readData() function")


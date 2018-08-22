import numpy as np
import pandas as pd



def readData(fileName):
    """
    Trying to read in raw data
    :param fileName:
    :return:
    """
    fs = open(fileName, "r")
    return fs.read().split()

"""
Statistical and time series analysis for bmorph modified time series.

Time series are expected to be in a pandas.Series object unless noted
otherwise. Reading and and writing is handled by the functions in ../io
"""

import numpy as np


def cunnane_pos(data):
    '''Cunnane plotting positions'''
    data = np.sort(data)
    ranks = (np.arange(data.size)+1)[::-1]
    quant = (ranks-0.4)/(data.size+0.2)  # Cunnane plotting position
    return quant

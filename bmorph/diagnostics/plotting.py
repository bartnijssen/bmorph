"""
Plotting for bmorph modified time series.

Time series are expected to be in a pandas.Series object unless noted
otherwise. Reading and and writing is handled by the functions in ../io
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

from .stats import cunnane_pos


def fdc_plot(data, label, ax, **kwargs):
    '''plotting positions for flow duration curve'''
    # plot on probability axis to stretch extremes
    quant = stats.norm.ppf(cunnane_pos(data))
    ax.plot(quant, np.sort(data), label=label, **kwargs)

    xminorticks = [0.00001, 0.00002, 0.00005, 0.0001, 0.0002, 0.0005,
                   0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.10, 0.20, 0.50,
                   0.80, 0.90, 0.95, 0.98, 0.99, 0.995, 0.098, 0.999,
                   0.9995, 0.0998, 0.9999, 0.99995, 0.09998, 0.99999]
    ax.set_xticks(stats.norm.ppf(xminorticks), minor=True)

    xmajorticks = [0.00001, 0.0001, 0.001, 0.01, 0.02, 0.05, 0.10, 0.20, 0.50,
                   0.80, 0.90, 0.95, 0.98, 0.99, 0.999, 0.9999, 0.99999]
    xticklabels = ['{0:g}'.format(100*x) for x in xmajorticks]
    ax.set_xticks(stats.norm.ppf(xmajorticks), minor=False)

    ax.set_xticklabels(xticklabels)
    ax.grid(True, which='both')

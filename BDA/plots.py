## script to set environment up


import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


message = """now importing: 
3. matplotlib.pyplot as plt
"""
print(message)

## set style
plt.style.use("ggplot") ## use plt.style.availalbe to see all styles
plt.style.use('seaborn-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6) ## set plot sizes


def _getcolor(val):
    colors = {0: "#E24A33", 1: "#348ABD", 2: "#988ED5", 3: "#777777", 
              4: "#FBC15E", 5: "#8EBA42", 6: "#FFB5B8", 7: "#E24A33"}
    color_choice = colors.get(val, val)
    return color_choice




def lines(x, y, linestyle='-', color = "#348ABD"):
    """Basic lines to current plot"""
    color_choice = _getcolor(color)
    tmp, = plt.plot(x, y, linestyle=linestyle, color=color_choice)
    return tmp



def plot(x, y, linestyle='-', color = "#348ABD", title="", xlabel="x", ylabel="y", ylim = None, xlim = None, show=True):
    """Basic line plots"""
    color_choice = _getcolor(color)
    tmp, = plt.plot(x, y, linestyle=linestyle, color=color_choice)
    plt.xticks(fontsize = 12)
    plt.yticks(fontsize = 12)
    plt.title(title, fontsize = 14)
    plt.ylabel(ylabel, fontsize = 13)
    plt.xlabel(xlabel, fontsize = 13)
    plt.ylim(ylim)
    plt.xlim(xlim)
    if show:
        plt.show()
        return tmp
    else:
        return tmp
    


def hist(x, bins='doane', xlabel = "X", ylabel = "Frequency", title = "Histogram",cumulative=False, density=True, color='0.3', edgecolor = 'white', show=True):
    """ Plot Histograms """
    color_choice = _getcolor(color)
    if isinstance(bins, str):
        breaks, _ =  np.histogram(a=x, bins=bins)
        bins = len(bins) * 2

    if density:
        #n = x.shape[0]
        w = np.ones_like(x) #/ n
        normed = True
        ylabel = "Density"
    else:
        normed=False
        w = np.ones_like(x)
        #ylabel = "Frequency"

    tmp = plt.hist(x, bins=bins, weights=w, cumulative=cumulative, color=color_choice,  edgecolor=edgecolor, normed=normed)
    plt.xticks(fontsize = 12) 
    plt.yticks(fontsize = 12)
    plt.ylabel(ylabel, fontsize = 13)
    plt.xlabel(xlabel, fontsize = 13)
    plt.title(title, fontsize = 14)
    if show:
        plt.show()
    else:
        return tmp


def cumMean(data):
    """ calculate cumulative mean """
    m = len(data)
    result = np.cumsum(data) / np.arange(1, m+1)
    return result

def cumSE(data):
    """ calculate cumulative standard error """
    m = len(data)
    mu = np.mean(data)
    num = np.sqrt(np.cumsum((data - mu)**2))
    denom = range(1, m+1)
    result = num/denom ## cummulative mean of (x_i - theta)**2
    return result




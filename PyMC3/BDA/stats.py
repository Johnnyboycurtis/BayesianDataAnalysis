## script to set environment up


import numpy as np
from scipy import stats

message = """now importing: 
1. numpy as np 
2. from scipy import stats

"""

print(message)


def summary(data, quantiles = [0, 25, 50, 75, 100], axis = 0):
    """ To print out summary statistics"""
    titles = " Min.:, 1st Qu.:, Median:, 3rd Qu.:, Max.:".split(",")
    percentiles = np.round(
        np.percentile(a=data, interpolation='midpoint', 
                      q=quantiles, 
                      axis = axis), 4)
    out = dict(zip(titles, percentiles))
    mean = np.round(np.mean(a = data, axis = axis), 4)
    out.update({" Mean:" : mean})
    for k, val in out.items():
        print(k, val)
    #return out

def table(data, prob=False):
    """Count unique values
    return a tuple(value, count)"""
    vals_counts = np.unique(ar=data, return_counts=True)
    if prob:
        density = vals_counts[1] / len(data)
        vals_counts = (vals_counts[0], density)
    out = tuple(zip(*vals_counts))
    return out




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



def dgamma(x, shape, rate = None, scale = 1, log = False):
    """
    The Gamma distribution with parameters ‘shape’ = a and ‘scale’ = s
    has density

                   f(x)= 1/(s^a Gamma(a)) x^(a-1) e^-(x/s)
                   
    If you want to use a rate, simply pass `scale = 1/rate`
    """
    if rate:
        scale = 1/rate
    val = stats.gamma.pdf(x, a=shape, loc=0, scale=scale)
    if log:
        return np.log(val)
    else:
        return val


def qgamma(p, shape, rate = None, scale = 1, lower_tail = True):
    """
    p: percentile (between 0 and 1)
    
    
    lower_tail: logical; if True (default), probabilities are P[X <= x],
          otherwise, P[X > x].
          
    The Gamma distribution with parameters ‘shape’ = a and ‘scale’ = s
    has density
    
                   f(x)= 1/(s^a Gamma(a)) x^(a-1) e^-(x/s)
                   
    If you want to use a rate, simply pass `scale = 1/rate`
    """
    if rate:
        scale = 1/rate
    if not lower_tail:
        p = 1 - p
    val = stats.gamma.ppf(q=p, a=shape, loc=0, scale=scale)
    return val
        
    



def priorGamma(mode, b, quantile, alpha=0.95):
    """
    Searches for appropriate Gamma distribution

    mode: numeric value for mode
    b: an array of potential rate parameters
    quantile: a quantile for the Gamma distribution to match `alpha` confidence level
    alpha: confidence level (usually 0.95)

    Returns (shape, rate)
    To obtain scale, scale = 1/rate
    """
    a = 1 + (mode * b)
    rate = b
    quants = qgamma(p = 0.95, shape = a, scale = 1/rate)
    MIN = np.min(quants)
    MAX = np.max(quants)
    if not (MIN <= quantile) and (quantile <= MAX):
        print(f"Could not find {quantile} within range of quantiles provided by `qgamma`; adjust `b` search space")
    diff = (quantile - quants)**2
    i = np.argmin(a=diff)
    return (a[i], b[i])
        


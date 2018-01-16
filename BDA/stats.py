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


######################################################################
######################## distribution functions ######################
######################################################################


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


def pgamma(q, shape, rate = None, scale = 1, lower_tail = True, log = False):
    """
    Example:
        > pgamma(0.3, shape = 2, rate = 2)
        [1] 0.1219014
    """
    if rate is not None:
        scale = 1/rate
    p = stats.gamma.cdf(x=q, a=shape, loc=0, scale=scale)
    if not lower_tail:
        p = 1-p
    if log:
        p = np.log(p)
    return p


def rgamma(n, shape, rate = None, scale = 1):
    if rate is not None:
        scale = 1/rate
    vals = np.random.gamma(shape = shape, scale = scale, size = n)
    return vals






def dbinom(x, size, prob, log=False):
    p = stats.binom.pmf(x, n=size, p=prob, loc=0)
    if log:
        p = np.log(p)
    return p


def pbinom(q, size, prob, lower_tail = True, log = False):
    p = stats.binom.cdf(k=q, n=size, p=prob, loc=0)
    if not lower_tail:
        p = 1 - p
    if log:
        p = np.log(p)
    return p


def qbinom(p, size, prob, lower_tail = True):
    """
    return quantile given a percentile (e.g. p=0.95)
    """
    if not lower_tail:
        p = 1-p
    q = stats.binom.ppf(q=p, n=size, p=prob, loc=0)
    return q



def rbinom(n, size, prob):
    vals = np.random.binomial(n=n, p=prob, size = size)
    return vals



def dbeta(x, shape1, shape2, ncp = 0, log = False):
    """
    The Beta distribution with parameters ‘shape1’ = a and ‘shape2’ = b has density

               Gamma(a+b)/(Gamma(a)Gamma(b)) x^(a-1) (1-x)^(b-1)

    for a > 0, b > 0 and 0 <= x <= 1 where the boundary values at x=0
     or x=1 are defined as by continuity (as limits).

    """

    pdf = stats.beta.pdf(x, a=shape1, b=shape2, loc=ncp, scale=1)
    return pdf


def pbeta(q, shape1, shape2, ncp = 0, lower_tail = True, log = False):
    p = stats.beta.cdf(x=q, a=shape1, b=shape2, loc=ncp, scale=1)
    if not lower_tail:
        p = 1-p
    if log:
        p = np.log(p)
    return p


def qbeta(p, shape1, shape2, ncp = 0, lower_tail = True, log = False):
    if not lower_tail:
        p = 1-p
    q = stats.beta.ppf(q=p, a=shape1, b=shape2, loc=ncp, scale=1)
    if log:
        q = np.log(q)
    return q


def rbeta(n, shape1, shape2):
    vals = np.random.beta(a=shape1,b=shape2,size=n)
    return vals





def dexp(x, rate = None, loc = 0, scale = 1, log = False):
    if rate:
        scale = 1/rate
    density = stats.expon.pdf(x, loc=loc, scale=scale)
    if log:
        density = np.log(density)
    return density


def pexp(q, rate = None, loc = 0, scale = 1, lower_tail = True, log = False):
    if rate:
        scale = 1/rate
    p = stats.expon.cdf(x=q, loc=loc, scale=scale)
    if not lower_tail:
        p = 1-p
    if log:
        p = np.log(p)
    return p


def qexp(p, rate = None, loc = 0, scale = 1, lower_tail = True, log = False):
    if rate:
        scale = 1/rate
    if not lower_tail:
        p = 1-p
    q = stats.expon.ppf(q=p, loc=loc, scale=scale)
    if log:
        q = np.log(q)
    return q

def rexp(n, rate = None, loc = 0, scale = 1, log = False):
    if rate:
        scale = 1/rate
    vals = np.random.exponential(scale = scale, size = n) + loc
    if log:
        vals = np.log(vals)
    return vals



######################################################################



    



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
        return ValueError(f"Could not find {quantile} within range of quantiles provided by `qgamma`; adjust `b` search space")
    diff = (quantile - quants)**2
    i = np.argmin(a=diff)
    return (a[i], b[i])
        


def Poisson_test(x1, x2, alternative = "two-sided"):
    if (not isinstance(x1, int)) or (not isinstance(x2, int)):
        print(f"{x1} or {x2} are not integers!")
    x= [x1, x2]
    pval = stats.binomial_test(x, sum(x), alternative = alternative)
    print(f"probability of success: {pval}")





def binom_test(x, n=None, p = 0.5, alternative = "greater", conflevel = 0.95):
    """
    Exact Binomial Test

    Parameters:
        x: int or list,array of length 2
        n: (optional) sum,total observations
        p: Null Hypothesis, default is 0.5
        alternative: less, greater or two-sided; default is `greater`
        conflevel: default is 0.95
    """
    def pLower(x, alpha):
        if (x == 0):  
            return 0 
        else:
            return qbeta(alpha, x, n - x +1)
    
    def pUpper(x, alpha):
        if(x == n):
            return 1
        else:
            return qbeta(1 - alpha, x+1, n-x)

    if isinstance(x, (list, np.ndarray, tuple)):
        if len(x) == 2:
            n = sum(x) ## sum the total values
            x = x[0] ## first value
        else:
            return ValueError("len(x) > 2")
    
    elif isinstance(x, int) :
        if n == None:
            return ValueError("n must be present and n > x")
    
    if alternative == "two-sided":
        relERROR = 1 + 0.00000001
        d = dbinom(x, n, p)
        m = n*p
        if (x == m):
            pval = 1 
        elif (x < m):
            i = np.arange(np.ceil(m), n+1)
            y = np.sum(dbinom(i, n, p) <= d * relERROR)
            pval = pbinom(x, n, p) + pbinom(n - y, n, p, lower_tail = False)
        else:
            i = np.arange(0, np.floor(m)+1)
            y = np.sum(dbinom(i, n, p) <= d*relERROR)
            pval = pbinom(y - 1, n, p) + pbinom(x - 1, n, p, lower_tail = False)
        alpha = (1 - conflevel)/2
        CI = (pLower(x, alpha), pUpper(x, alpha))
        
    elif (alternative == "less"):
        pval = pbinom(x, n, p)
        CI = (0, pUpper(x, 1 - conflevel))
    
    elif (alternative == "greater"):
        pval = pbinom(x - 1, n, p, lower_tail = False)
        CI = (pLower(x, 1 - conflevel), 1)
    
    ESTIMATE = x/n

    result = f"""
    	Exact binomial test

        number of successes = {x}, number of trials = {n}, p-value = {pval}
        alternative hypothesis: true probability of success is greater than {p}
        95 percent confidence interval:
        {CI}
        probability of success: {ESTIMATE}
    """
    print(result)

    return {'stat':ESTIMATE, 'conf-interval': CI, 'p-val':pval}
    


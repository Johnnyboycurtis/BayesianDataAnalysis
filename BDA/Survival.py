import numpy as np
import matplotlib.pyplot as plt


from collections import namedtuple

survival = namedtuple('Survival', ['time', 'censored'], verbose=False) ## set True if you want to see code




class KaplanMeier():
    def __init__(self, times=None, censored=None, data = None, verbose=False):
        if data:
            self.data = data
        else:
            self.data = [survival(t,d) for t,d in zip(times, censored)]
        self.estimates = self.KP_estimate(verbose)

    def KP_estimate(self, verbose=False):
        ## create bins from non-censored data
        data = self.data
        tmp = list(set([x.time for x in data if x.censored == 0]))
        tmp.sort()
        a = 0
        bins = []
        
        while tmp:
            b = tmp.pop(0)
            bins.append((a,b))
            a = b
        bins.append((a, np.inf))
        
        total_survivors = []
        surv_rate = 1
        for a, b in bins:
            alive, dead = check_alive(a,b, data, verbose=verbose)
            surv_rate *= (1 - dead/alive)
            total_survivors.append((a,b, alive, dead, round(surv_rate, 3)))
        return total_survivors

    def __repr__(self):
        est =  self.estimates
        #header = "
        est_out = "\n".join([str(i) for i in est])
        #out = header + out
        out = f"a, b, previously alive, dead, rate \n{est_out}"
        return out

    def plot(self, method = 'step'):
        surv_rates = [x[4] for x in self.estimates]
        time = [x[0] for x in self.estimates]
        if method == 'line':
            plt.plot(time, surv_rates, "--")
        elif method == 'step':
            plt.step(time, surv_rates)
        plt.xlabel("Time")
        plt.ylabel("Survival Rate")
        plt.title("Kaplan-Meier Estimates")
        plt.show()
            


def check_alive(a, b, data, verbose = False):
    dead = 0
    alive = 0 ## previously alive
    for time, censored in data:
        result = (a <= time) and (time < b) and (censored == 0)
        if result:
            dead += 1
        if time >= a:
            alive +=1
        if verbose:
            print(f"{a} - <{b}: ({time}, {censored}) : {alive}, {dead}")
    #print(alive, dead)
    return (alive, dead)


"""
times = [6, 6, 6, 6, 7, 9, 10, 10, 11, 13, 16,
        17, 19, 20, 22, 23, 25, 32, 32, 34, 35]

censored = [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0,
            1, 1, 1, 0, 0, 1, 1, 1, 1, 1]


surv = KaplanMeier(times, censored)

print(surv)

surv.plot()
""" 







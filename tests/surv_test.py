import sys
sys.path.append('../')

from BDA import Survival

with open("./../data/kidney.csv") as myfile:
    header = myfile.readline()
    time = []
    status = []
    for line in myfile:
        data = line.strip().split(',')
        time.append(int(data[1]))
        status.append(int(data[2]))




treated = [Survival.survival(t, d) for t,d in zip(time, status)]

fit = Survival.KaplanMeier(data = treated, times = None, censored = None)

print(fit)


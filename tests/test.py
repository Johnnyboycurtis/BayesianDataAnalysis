import sys
sys.path.append('../')
from BDA import stats

stats.binom_test(x = 10, n = 30, p = 0.5, alternative = "greater")
stats.binom_test(x = [10, 20], p = 0.5, alternative = "greater")
#binom.test(x = 10, n = 30, p = 0.5, alternative = "greater")  ## R



stats.binom_test(x = 10, n = 30, p = 0.5, alternative = "less")
stats.binom_test(x = [10, 20], p = 0.5, alternative = "less")
#binom.test(x = 10, n = 30, p = 0.5, alternative = "less")  ## R



stats.binom_test(x = 10, n = 30, p = 0.5, alternative = "two-sided")
stats.binom_test(x = [10, 20], p = 0.5, alternative = "two-sided")
#binom.test(x = 10, n = 30, p = 0.5, alternative = "two.sided")  ## R

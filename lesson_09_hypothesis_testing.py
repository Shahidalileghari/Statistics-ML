"""
LESSON 09 — Hypothesis testing and p-values
Two-sided one-sample t-test against a prespecified benchmark of 75.
A p-value is P(data at least this incompatible with H0 | H0 and assumptions), not
P(H0 is true). Report effect size and interval, not p-value alone.
"""
import numpy as np
from scipy import stats
scores=np.array([78,81,74,77,83,79,76,80,72,82,78,85],dtype=float)
benchmark=75
result=stats.ttest_1samp(scores,popmean=benchmark)
difference=scores.mean()-benchmark
print("Sample mean:",scores.mean())
print("Difference from benchmark:",difference)
print("t statistic:",result.statistic)
print("p-value:",result.pvalue)
print("Interpretation: assess evidence against H0 alongside effect size, interval, design and assumptions.")

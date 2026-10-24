"""
LESSON 08 — Confidence intervals for a mean
Example uses a t interval because population SD is unknown.
Frequentist interpretation: across repeated samples, 95% of intervals built this way
would cover the fixed population mean, assuming the method's conditions hold.
"""
import numpy as np
from scipy import stats
scores=np.array([72,75,78,81,69,88,76,74,83,79,71,85],dtype=float)
n=len(scores);mean=scores.mean();se=stats.sem(scores)
lo,hi=stats.t.interval(.95,df=n-1,loc=mean,scale=se)
print(f"n={n}, mean={mean:.2f}, SE={se:.2f}")
print(f"95% t confidence interval: [{lo:.2f}, {hi:.2f}]")
print("Discuss: What changes if the sample is biased or observations are dependent?")

"""
LESSON 06 — Bernoulli, binomial, normal and Poisson distributions
Use SciPy for probability calculations; use simulations to build intuition.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path
OUT=Path("visualizations");OUT.mkdir(exist_ok=True)
# Binomial: 10 independent attempts, success probability .3
n,p=10,.3
k=np.arange(n+1)
pmf=stats.binom.pmf(k,n,p)
print("P(exactly 4 successes):",stats.binom.pmf(4,n,p))
# Poisson: count of events with average rate 3 per interval
print("P(exactly 0 events when lambda=3):",stats.poisson.pmf(0,3))
# Normal: standardize an observation
x,mu,sigma=85,70,10
z=(x-mu)/sigma
print(f"z-score for x={x}: {z:.2f}")
fig,ax=plt.subplots(figsize=(7,4));ax.bar(k,pmf)
ax.set(title="Binomial distribution: n=10, p=0.3",xlabel="Number of successes",ylabel="Probability")
fig.tight_layout();fig.savefig(OUT/"lesson_06_binomial_pmf.png",dpi=160);plt.show()

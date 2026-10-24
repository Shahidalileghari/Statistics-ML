"""
LESSON 07 — Sampling, standard error and Central Limit Theorem
The standard deviation describes individual observations; standard error describes
the sampling variability of an estimator (here, the sample mean).
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
OUT=Path("visualizations");OUT.mkdir(exist_ok=True)
rng=np.random.default_rng(101)
population=rng.exponential(scale=2,size=100_000) # skewed population
means=[]
for _ in range(5000):
    means.append(rng.choice(population,size=40,replace=True).mean())
print("Population mean:",population.mean())
print("Mean of sample means:",np.mean(means))
print("Empirical SE:",np.std(means,ddof=1))
print("Theory SE ≈ population SD/sqrt(n):",population.std(ddof=1)/np.sqrt(40))
fig,ax=plt.subplots(figsize=(7,4));ax.hist(means,bins=40,edgecolor="white")
ax.set(title="Sampling distribution of sample mean (n=40)",xlabel="Sample mean",ylabel="Frequency")
fig.tight_layout();fig.savefig(OUT/"lesson_07_clt.png",dpi=160);plt.show()

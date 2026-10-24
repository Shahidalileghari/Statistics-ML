"""
LESSON 14 — Bootstrap confidence intervals
Resample observations with replacement to approximate an estimator's sampling distribution.
Bootstrap is useful, but not magic: representativeness and dependence still matter.
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
OUT=Path("visualizations");OUT.mkdir(exist_ok=True)
rng=np.random.default_rng(42)
data=np.array([12,15,14,18,19,11,16,17,15,14,22,13,16,18],dtype=float)
B=5000
boot_means=np.array([rng.choice(data,size=len(data),replace=True).mean() for _ in range(B)])
lo,hi=np.quantile(boot_means,[.025,.975])
print("Observed mean:",data.mean())
print(f"Percentile bootstrap 95% interval: [{lo:.2f}, {hi:.2f}]")
fig,ax=plt.subplots(figsize=(7,4));ax.hist(boot_means,bins=35,edgecolor="white")
ax.axvline(lo,linestyle="--");ax.axvline(hi,linestyle="--")
ax.set(title="Bootstrap distribution of the sample mean",xlabel="Bootstrap mean",ylabel="Frequency")
fig.tight_layout();fig.savefig(OUT/"lesson_14_bootstrap.png",dpi=160);plt.show()

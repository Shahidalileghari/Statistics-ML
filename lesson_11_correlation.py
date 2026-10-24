"""
LESSON 11 — Covariance, Pearson correlation and Spearman rank correlation
Correlation describes association; it does not prove causality.
Pearson captures linear association and is sensitive to influential outliers.
"""
import numpy as np
from scipy.stats import pearsonr,spearmanr
import matplotlib.pyplot as plt
from pathlib import Path
OUT=Path("visualizations");OUT.mkdir(exist_ok=True)
rng=np.random.default_rng(14)
x=np.linspace(1,10,60)
y=5+4*x+rng.normal(0,7,size=len(x))
print("Pearson:",pearsonr(x,y))
print("Spearman:",spearmanr(x,y))
fig,ax=plt.subplots(figsize=(7,4));ax.scatter(x,y)
ax.set(title="Positive association (synthetic data)",xlabel="Practice hours",ylabel="Assessment score")
fig.tight_layout();fig.savefig(OUT/"lesson_11_correlation.png",dpi=160);plt.show()

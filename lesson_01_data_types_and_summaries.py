"""
LESSON 01 — Data types and descriptive summaries
Topics: categorical/numeric data, mean, median, mode, range, variance, SD, IQR, quantiles.
Worked example includes one extreme value to compare mean and median.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
OUT = Path("visualizations"); OUT.mkdir(exist_ok=True)

hours = np.array([1.0, 1.5, 2.0, 2.0, 2.5, 3.0, 3.5, 4.0, 18.0])
s = pd.Series(hours, name="study_hours")
print("Mean:", s.mean())
print("Median:", s.median())
print("Sample variance (ddof=1):", s.var())
print("Sample standard deviation:", s.std())
print("Q1, median, Q3:", s.quantile([.25, .5, .75]).to_dict())
print("IQR:", s.quantile(.75) - s.quantile(.25))

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].hist(hours, bins=8, edgecolor="black")
axes[0].set(title="Study hours", xlabel="Hours", ylabel="Frequency")
axes[1].boxplot(hours, vert=True)
axes[1].set(title="Box plot reveals an extreme value", ylabel="Hours")
fig.tight_layout(); fig.savefig(OUT/"lesson_01_center_spread.png", dpi=160); plt.show()

# Student practice:
# 1. Remove 18.0 and recalculate mean/median.
# 2. Explain why the median changes less than the mean.
# 3. Is 18.0 necessarily an error? What context would you need?

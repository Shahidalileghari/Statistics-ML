"""
LESSON 10 — Comparing two independent groups
Welch's t-test does not assume equal population variances.
Synthetic example: two teaching methods, with score outcomes.
"""
import numpy as np
from scipy import stats
A=np.array([72,75,78,80,69,74,77,81,73,76],dtype=float)
B=np.array([76,79,82,85,74,80,83,78,81,77],dtype=float)
res=stats.ttest_ind(B,A,equal_var=False)
print(f"Group A mean={A.mean():.2f}; Group B mean={B.mean():.2f}")
print(f"Difference B-A={B.mean()-A.mean():.2f}")
print(f"Welch t={res.statistic:.3f}, p={res.pvalue:.4f}")
print("Discuss confounding: were students randomly assigned, or could prior ability differ?")

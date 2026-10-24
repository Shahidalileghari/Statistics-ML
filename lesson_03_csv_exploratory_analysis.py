"""
LESSON 03 — Guided exploratory data analysis with the course CSV
Run from course root: python 01_Descriptive_Statistics/lesson_03_csv_exploratory_analysis.py
"""
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
data_path=Path("datasets/synthetic_student_performance.csv")
out=Path("visualizations");out.mkdir(exist_ok=True)
df=pd.read_csv(data_path)
print("Shape:",df.shape)
print("\nTypes:\n",df.dtypes)
print("\nMissing values:\n",df.isna().sum())
print("\nSummary:\n",df.describe().round(2))
print("\nPass rate:",df["passed"].mean())
fig,axes=plt.subplots(1,2,figsize=(10,4))
axes[0].hist(df["final_score"],bins=12,edgecolor="white")
axes[0].set(title="Final score distribution",xlabel="Score",ylabel="Count")
axes[1].scatter(df["practice_hours_per_week"],df["final_score"],alpha=.65)
axes[1].set(title="Practice vs final score",xlabel="Practice hours/week",ylabel="Final score")
fig.tight_layout();fig.savefig(out/"lesson_03_csv_eda.png",dpi=160);plt.show()

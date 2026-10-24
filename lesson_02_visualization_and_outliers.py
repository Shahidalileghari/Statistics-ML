"""
LESSON 02 — Choosing visualizations and investigating outliers
Rule of thumb: histogram for one numeric variable; bar chart for categories;
scatterplot for two numeric variables; boxplot for spread/outlier screening.
An outlier is a flag for investigation, not an automatic deletion instruction.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
OUT=Path("visualizations"); OUT.mkdir(exist_ok=True)
rng=np.random.default_rng(7)
df=pd.DataFrame({"study_hours":rng.normal(4,1.2,120).clip(0),
                 "exam_score":rng.normal(70,10,120).clip(0,100)})
df.loc[5,"study_hours"]=12
df.loc[5,"exam_score"]=98
q1,q3=df.study_hours.quantile([.25,.75]); iqr=q3-q1
lo,hi=q1-1.5*iqr,q3+1.5*iqr
print(f"IQR fences for study_hours: [{lo:.2f}, {hi:.2f}]")
print("Flagged rows:\n",df[(df.study_hours<lo)|(df.study_hours>hi)])
fig,ax=plt.subplots(figsize=(7,4))
ax.scatter(df.study_hours,df.exam_score,alpha=.7)
ax.set(title="Study time and exam score (synthetic data)",xlabel="Study hours",ylabel="Exam score")
fig.tight_layout();fig.savefig(OUT/"lesson_02_scatter_outlier.png",dpi=160);plt.show()

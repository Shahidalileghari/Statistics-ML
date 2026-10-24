"""
CAPSTONE — From question to statistical report
Question: Is there an association between practice hours and assessment scores?
This synthetic analysis demonstrates visualization, summary statistics, correlation,
regression, limitations and a report-ready conclusion.
"""
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from pathlib import Path
OUT=Path("visualizations");OUT.mkdir(exist_ok=True)
rng=np.random.default_rng(2026)
df=pd.DataFrame({"practice_hours":rng.uniform(0,12,160)})
df["score"]=(48+3.6*df.practice_hours+rng.normal(0,9,160)).clip(0,100)
print(df.describe().round(2))
r,p=pearsonr(df.practice_hours,df.score)
model=LinearRegression().fit(df[["practice_hours"]],df.score)
print(f"Pearson r={r:.3f}, p={p:.4g}")
print(f"Regression slope={model.coef_[0]:.2f} score points/hour; R²={r2_score(df.score,model.predict(df[['practice_hours']])):.3f}")
fig,ax=plt.subplots(figsize=(7,4))
ax.scatter(df.practice_hours,df.score,alpha=.6)
x=np.linspace(df.practice_hours.min(),df.practice_hours.max(),100)
ax.plot(x,model.predict(pd.DataFrame({"practice_hours":x})))
ax.set(title="Capstone: practice time and score (synthetic)",xlabel="Practice hours",ylabel="Score")
fig.tight_layout();fig.savefig(OUT/"capstone_practice_score.png",dpi=160);plt.show()
print("\nConclusion template: In this synthetic sample, practice hours were [positively/negatively] associated with score.")
print("Do not claim causation: motivation, prior knowledge, and study quality may confound the relationship.")

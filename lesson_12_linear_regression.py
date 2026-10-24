"""
LESSON 12 — Simple linear regression, residuals and R-squared
Fit score ~ study_hours. A fitted line summarizes conditional mean trends; it does
not establish a causal effect without a defensible design and assumptions.
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from pathlib import Path
OUT=Path("visualizations");OUT.mkdir(exist_ok=True)
rng=np.random.default_rng(33)
X=np.linspace(0,10,100).reshape(-1,1)
y=50+4.2*X.ravel()+rng.normal(0,7,size=100)
model=LinearRegression().fit(X,y);pred=model.predict(X);resid=y-pred
print("Intercept:",model.intercept_,"Slope:",model.coef_[0])
print("R²:",r2_score(y,pred),"RMSE:",mean_squared_error(y,pred)**0.5)
fig,axes=plt.subplots(1,2,figsize=(10,4))
axes[0].scatter(X,y,alpha=.7);axes[0].plot(X,pred);axes[0].set(xlabel="Study hours",ylabel="Score",title="Fitted regression")
axes[1].scatter(pred,resid,alpha=.7);axes[1].axhline(0,linestyle="--");axes[1].set(xlabel="Predicted score",ylabel="Residual",title="Residual diagnostic")
fig.tight_layout();fig.savefig(OUT/"lesson_12_regression_diagnostics.png",dpi=160);plt.show()

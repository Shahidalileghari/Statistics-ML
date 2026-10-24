"""
LESSON 00 — A reproducible Python workflow
Objectives:
- Use a random seed for repeatable examples.
- Represent observations with NumPy and pandas.
- Produce a basic descriptive summary and plot.
Worked example: quiz scores for a small fictional class.
Run: python 00_Getting_Started/lesson_00_python_statistics_workflow.py
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path("visualizations")
OUT.mkdir(exist_ok=True)
rng = np.random.default_rng(42)  # reproducible pseudo-random generator

scores = np.array([62, 68, 71, 71, 75, 79, 84, 90, 94, 96])
df = pd.DataFrame({"student_id": range(1, len(scores)+1), "score": scores})
print("First rows:\n", df.head())
print("\nDescriptive summary:\n", df["score"].describe())
print("\nMean:", df["score"].mean(), "| Median:", df["score"].median())

fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(scores, bins=6, edgecolor="black")
ax.set(title="Quiz-score distribution (fictional data)", xlabel="Score", ylabel="Number of students")
fig.tight_layout()
fig.savefig(OUT / "lesson_00_quiz_scores.png", dpi=160)
plt.show()

# Quick check:
# Why is a random seed useful in teaching and reproducible analysis?

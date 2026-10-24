# Statistics for Data Science, AI & Machine Learning
**Instructor-ready course | Python-first | Topic-by-topic | Worked examples + visualizations**

## Course outcomes
By the end, learners should be able to:
- describe and visualize data without confusing sample and population quantities;
- reason about probability, conditional probability, Bayes' theorem, and random variables;
- use common probability distributions and the Central Limit Theorem;
- estimate parameters, construct confidence intervals, and perform hypothesis tests;
- interpret correlation and regression without making causal claims from association alone;
- understand statistical ideas behind evaluation metrics, data leakage, uncertainty, and model comparison;
- design and interpret basic A/B tests;
- complete a reproducible statistical analysis with Python.

## Recommended environment
Python 3.10+ recommended. Install dependencies:
```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
```
Run scripts from the course root. Jupyter is optional:
```bash
jupyter lab
```

## Learning pattern used in every lesson
1. Learning objectives
2. Intuition and definitions
3. Worked numerical example
4. Mathematical interpretation
5. Python implementation
6. Visualization where it helps
7. Student practice
8. Instructor solution / discussion prompts

## Course map
| Module | Topics | Suggested time |
|---|---|---:|
| 00 | Setup, reproducibility, Python workflow | 1 hour |
| 01 | Data types, center, spread, quantiles, outliers, visualization | 4–5 hours |
| 02 | Events, rules, conditional probability, independence, Bayes | 4 hours |
| 03 | Random variables, expectation, variance, Bernoulli/binomial/normal/Poisson | 5 hours |
| 04 | Sampling, sampling distributions, standard error, CLT | 3 hours |
| 05 | Estimation, confidence intervals, p-values, tests, effect size | 5 hours |
| 06 | Covariance, correlation, simple/multiple regression, residuals | 4 hours |
| 07 | Statistical thinking in ML, metrics, leakage, bootstrap, calibration | 5 hours |
| 08 | Bayesian reasoning, priors, likelihood, posterior | 3 hours |
| 09 | A/B testing, experiment design, power and practical significance | 3 hours |
| 10 | Capstone, rubric, assessment bank | 4–6 hours |

**Total:** approximately 37–42 teaching hours, plus practice.

## Folder guide
- Numbered module folders contain runnable lesson scripts.
- `datasets/` contains small, clearly labeled teaching datasets (synthetic unless stated otherwise).
- `visualizations/` is the default output folder for plots.
- `instructor_resources/` contains lesson plans, solutions, assessment prompts, and a capstone rubric.
- Every script prints key values and creates plots where useful.

## Important teaching cautions
- Statistical significance is not the same as practical importance.
- A p-value is not the probability that the null hypothesis is true.
- Correlation does not establish causation.
- A confidence interval procedure has a long-run coverage interpretation; it does not mean a fixed parameter has a 95% probability of lying in one realized frequentist interval.
- A model's test set must not influence training, feature selection, preprocessing decisions, or tuning.
- Assumptions matter: discuss independence, sampling design, distributional conditions, and measurement quality.
- Synthetic datasets are for instruction and are not evidence about real populations.

## Suggested teaching rhythm
For a 90-minute class: 10 min retrieval quiz, 20 min concept, 25 min worked example, 20 min guided coding/plot, 10 min student practice, 5 min exit ticket.

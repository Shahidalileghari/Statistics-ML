# Instructor Guide

## Teaching principles
- Ask students to predict an answer before running code.
- Separate the statistical question from the software implementation.
- Require interpretation in plain language after every numeric result.
- Ask what assumptions and data-collection choices could invalidate the conclusion.
- Prefer reproducible scripts and explicit random seeds for demonstrations.

## Suggested assessment weighting
- Weekly concept checks and short calculations: 15%
- Python labs and visualization interpretation: 25%
- Mid-course inference assignment: 20%
- Capstone report and presentation: 30%
- Reproducibility, documentation, and peer review: 10%

## Rubric (100 points)
| Criterion | Points | Strong performance |
|---|---:|---|
| Question and study design | 15 | Clear question, target population, variables, sampling limitations |
| Data quality and EDA | 15 | Checks missingness, types, unusual values; appropriate plots |
| Statistical method | 20 | Method matches design and assumptions are discussed |
| Python reproducibility | 15 | Runnable code, dependencies, seeds, clear outputs |
| Interpretation | 20 | Correct uncertainty/effect-size interpretation; no causal overclaim |
| Communication | 10 | Clear tables, labeled plots, accessible narrative |
| Limitations | 5 | Specific limitations and next steps |

## Discussion prompts
1. When can the mean be misleading?
2. Why does conditional probability reverse intuition in low-prevalence settings?
3. What is the difference between SD and SE?
4. What does a p-value not tell us?
5. Why can a tiny effect be statistically significant with a huge sample?
6. How can data leakage inflate a model's apparent performance?
7. What makes an A/B test invalid even if its p-value is small?

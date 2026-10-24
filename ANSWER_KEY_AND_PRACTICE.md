# Student Practice and Instructor Notes

## Module 1 — Descriptive statistics
1. Remove the extreme value 18 from the study-hours list and compare mean/median.
   **Expected insight:** mean shifts more because it uses every value's magnitude; median is rank-based.
2. Can a boxplot prove an observation is erroneous?
   **No.** It flags unusual values; investigate provenance and domain context.

## Module 2 — Probability
1. P(A)=0.6, P(B)=0.5, P(A∩B)=0.3. Are A and B independent?
   **Yes**, because 0.6×0.5=0.3.
2. Explain why P(Disease | positive) differs from P(positive | Disease).
   **They condition on different events**; prevalence and false-positive rate matter.

## Module 3 — Distributions
1. Why can the expected value of a die roll be 3.5 although no roll equals 3.5?
   **Expectation is a long-run weighted average, not necessarily a possible outcome.**
2. Give an example where Poisson might be a useful approximation and name its assumptions.

## Module 4 — Sampling
1. What happens to the standard error of a mean if sample size grows by a factor of 4?
   **It halves**, if the standard deviation and sampling design stay comparable.
2. Does the CLT make biased sampling harmless?
   **No.** It concerns sampling-distribution behavior, not correction of selection bias.

## Module 5 — Inference
1. Interpret a 95% confidence interval using long-run coverage.
2. Why should effect size and uncertainty accompany a p-value?
3. State one way multiple testing can increase false positives.

## Module 6 — Regression
1. Explain why correlation does not imply causation.
2. What residual pattern might suggest nonlinearity or unequal variance?
3. Why is extrapolating beyond the observed x-range risky?

## Module 7 — ML statistics
1. Which metric is useful when positive cases are rare and missing a positive is costly?
   **Recall may be central**, but thresholds and precision/recall trade-offs should be discussed.
2. Give two examples of data leakage.
   **Examples:** scaling before splitting; selecting features using the test set; target-derived columns.

## Module 8 — Bayesian reasoning
1. Explain how prior information and observed data contribute to the posterior.
2. Does a prior have to be subjective? Discuss weakly informative and domain-informed priors.

## Module 9 — A/B testing
1. Distinguish absolute lift from relative lift.
2. Why predefine a stopping rule and primary metric?
3. Why might a statistically significant result still be a poor product decision?

## Capstone extension
Use a public or instructor-provided dataset. Submit:
- question and target population;
- data dictionary and cleaning log;
- at least three informative visualizations;
- descriptive statistics;
- justified inferential/modeling method;
- effect size and uncertainty;
- limitations, ethics/privacy notes, and a plain-language conclusion;
- reproducible code and requirements file.

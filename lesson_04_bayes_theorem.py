"""
LESSON 04 — Bayes' theorem and base rates
P(D|+)=P(+|D)P(D) / [P(+|D)P(D)+P(+|not D)P(not D)]
Teaching point: a highly accurate test can still yield many false positives when prevalence is low.
"""
prevalence=0.01
sensitivity=0.95
specificity=0.90
p_pos=(sensitivity*prevalence)+((1-specificity)*(1-prevalence))
posterior=(sensitivity*prevalence)/p_pos
print(f"Probability of positive test: {p_pos:.3%}")
print(f"Probability of disease given positive test: {posterior:.3%}")
# Natural frequency view for 10,000 people:
n=10_000
true_pos=n*prevalence*sensitivity
false_pos=n*(1-prevalence)*(1-specificity)
print(f"Out of {n:,}: true positives ≈ {true_pos:.0f}; false positives ≈ {false_pos:.0f}")
print(f"Positive results that are true positives: {true_pos/(true_pos+false_pos):.1%}")

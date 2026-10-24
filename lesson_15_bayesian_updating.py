"""
LESSON 15 — Bayesian updating with a Beta-Binomial model
For Bernoulli success probability p, use Beta(alpha,beta) prior.
After s successes and f failures, posterior is Beta(alpha+s,beta+f).
This is a compact, conjugate example suitable for teaching.
"""
from scipy.stats import beta
alpha,beta_prior=2,2
successes,failures=8,12
post_a=alpha+successes;post_b=beta_prior+failures
print("Prior mean:",alpha/(alpha+beta_prior))
print("Posterior mean:",post_a/(post_a+post_b))
print("Posterior 95% credible interval:",beta.ppf([.025,.975],post_a,post_b))
print("Contrast: credible intervals use a probability statement about the parameter under the posterior model.")

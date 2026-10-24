"""
LESSON 16 — A/B testing: conversion rates and interpretation
Synthetic example comparing two independent conversion proportions.
Before testing: define primary metric, randomization unit, sample size, duration,
guardrail metrics and stopping rule. Avoid repeatedly checking and stopping casually.
"""
import numpy as np
from statsmodels.stats.proportion import proportions_ztest,confint_proportions_2indep
# A: 120 conversions / 2000 visitors; B: 145 / 2000 visitors
counts=np.array([120,145]);nobs=np.array([2000,2000])
z,p=proportions_ztest(counts,nobs)
ci=confint_proportions_2indep(counts[1],nobs[1],counts[0],nobs[0],method="newcomb")
print("A conversion rate:",counts[0]/nobs[0])
print("B conversion rate:",counts[1]/nobs[1])
print("Absolute lift:",counts[1]/nobs[1]-counts[0]/nobs[0])
print("Relative lift:",(counts[1]/nobs[1])/(counts[0]/nobs[0])-1)
print("z:",z,"p-value:",p)
print("Approx. 95% CI for B-A:",ci)
print("Statistical evidence does not automatically mean the change is worth shipping.")

"""
LESSON 05 — Random variables, expectation and variance
A random variable maps outcomes to numbers. E[X] is a probability-weighted average.
For a fair six-sided die, E[X]=3.5 even though 3.5 cannot occur on one roll.
"""
import numpy as np
outcomes=np.arange(1,7)
probs=np.repeat(1/6,6)
expected=np.sum(outcomes*probs)
variance=np.sum((outcomes-expected)**2*probs)
print("Expected value:",expected)
print("Variance:",variance)
rng=np.random.default_rng(21)
rolls=rng.choice(outcomes,size=100_000,p=probs)
print("Simulation mean:",rolls.mean(),"Simulation variance:",rolls.var())

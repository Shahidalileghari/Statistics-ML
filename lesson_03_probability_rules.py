"""
LESSON 03 — Probability rules and conditional probability
P(A or B)=P(A)+P(B)-P(A and B)
P(A|B)=P(A and B)/P(B), when P(B)>0
Independence means P(A and B)=P(A)P(B), not merely that events seem unrelated.
"""
# Example: 100 students; 40 study Python, 30 study SQL, 15 study both.
p_python=40/100; p_sql=30/100; p_both=15/100
p_either=p_python+p_sql-p_both
p_python_given_sql=p_both/p_sql
print(f"P(Python or SQL) = {p_either:.2f}")
print(f"P(Python | SQL) = {p_python_given_sql:.2f}")
print("Independence check:", p_both, "versus", p_python*p_sql)
print("Because these are unequal, the events are not independent in this dataset.")
# Practice: If P(A)=.6, P(B)=.5, P(A∩B)=.3, are A and B independent?

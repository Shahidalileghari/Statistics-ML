"""
LESSON 13 — Statistical thinking for machine learning evaluation
Use a held-out test set once for final evaluation. This example compares classification
metrics and shows why accuracy can mislead on imbalanced data.
"""
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
y_true=[1]*10+[0]*90
y_pred=[0]*100 # classifier predicts only the majority class
print("Accuracy:",accuracy_score(y_true,y_pred))
print("Precision (positive class):",precision_score(y_true,y_pred,zero_division=0))
print("Recall (positive class):",recall_score(y_true,y_pred,zero_division=0))
print("F1:",f1_score(y_true,y_pred,zero_division=0))
print("Confusion matrix:\n",confusion_matrix(y_true,y_pred))
print("Teaching point: metric choice must reflect error costs and the task.")

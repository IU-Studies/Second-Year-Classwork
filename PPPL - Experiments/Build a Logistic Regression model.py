#Build a Logistic Regression model using Scikit-learn to classify students into "Pass"
#or "Fail" categories based on their study hours. Train the model on a dataset and
#evaluate its performance using metrics such as accuracy score and confusion matrix.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

file_path = r"C:\Users\iu\Downloads\student_exam_data.csv"
df = pd.read_csv(file_path)
X = df[['Study Hours']]
y = df['Pass/Fail']

xtrain, xtest, trainy, testy = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(xtrain, trainy)
ypre = model.predict(xtest)
accuracy = accuracy_score(testy, ypre)
cmat = confusion_matrix(testy, ypre)

print("Accuracy Score ", accuracy)
print("Confusion Matrix ", cmat)
print("Classification Report: ", classification_report(testy, ypre))

plt.figure(figsize=(8, 6))
sns.scatterplot(x=xtrain['Study Hours'], y=trainy, label="Training Data", color='blue')
sns.scatterplot(x=xtest['Study Hours'], y=testy, label="Test Data", color='red')

X_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_prob = model.predict_proba(X_range)[:, 1]
plt.plot(X_range, y_prob, color='green', label="Logistic Regression Curve")

plt.xlabel("Study Hours")
plt.ylabel("Probability of Passing")
plt.legend()
plt.title("Logistic Regression Model for Study Hours vs Pass/Fail")
plt.show()

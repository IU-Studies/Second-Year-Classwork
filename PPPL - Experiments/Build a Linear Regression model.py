# Build a Linear Regression model using Scikit-learn to predict student scores based
# on study hours and evaluate its performance using mean squared error.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv(r"C:\Users\iu\Downloads\score.csv")
X = df[["Hours"]]
y = df["Scores"]

trainx, testx, trainy, testy = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(trainx, trainy)
predicty = model.predict(testx)
mse = mean_squared_error(testy, predicty)

print(f"Mean Squared Error: {mse:.2f}")

plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Linear Regression: Study Hours vs. Exam Score")
plt.legend()
plt.show()


"""
#Simple approach

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv("C:/Users/IU/Downloads/score.csv")

X = df[["Hours"]]
y = df["Scores"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression().fit(X_train, y_train)

y_pred = model.predict(X_test)
print(mean_squared_error(y_test, y_pred))

plt.scatter(X, y)
plt.plot(X, model.predict(X), color='red')
plt.show()
"""

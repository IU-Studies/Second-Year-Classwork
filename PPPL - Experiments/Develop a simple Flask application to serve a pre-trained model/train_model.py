import pickle
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])  # y = 2x

model = LinearRegression()
model.fit(X, y)

with open('linear_model.pkl', 'wb') as f:
    pickle.dump(model, f)

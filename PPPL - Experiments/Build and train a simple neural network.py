#Build and train a simple neural network using TensorFlow to classify binary data.
#The dataset consists of three input features and two output classes. Use the
#following architecture for your neural network:
#• Input Layer: Accepts three features per data point.
#• Hidden Layer: Contains 10 neurons with the ReLU activation function.
#Output Layer: Contains two neurons with the softmax activation function for binary classification.

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from tensorflow.keras.utils import to_categorical
X, y = make_classification(n_samples=1000, n_features=3, n_informative=3,
n_redundant=0, n_classes=2, random_state=42)
y_categorical = to_categorical(y, num_classes=2)
X_train, X_test, y_train, y_test = train_test_split(X, y_categorical, test_size=0.2, random_state=42)
model = Sequential([
Dense(10, activation='relu', input_shape=(3,)),
Dense(2, activation='softmax')
])
model.compile(optimizer='adam',
loss='categorical_crossentropy',
metrics=['accuracy'])
model.fit(X_train, y_train, epochs=20, batch_size=16, validation_split=0.1)
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy:.2f}")

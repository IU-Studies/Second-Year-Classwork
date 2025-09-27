# Create a bar plot and scatter plot to visualize relationships in a dataset using Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\IU\Downloads\iris.csv")

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='species',hue='species', palette='Set2')
plt.title('Count Iris Species')
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species', palette='Set2')
plt.title('Sepal Length and Sepal Width')
plt.show()


""" 
#Simple approach

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\IU\Downloads\iris.csv")

sns.countplot(x = df['species'])
plt.show()

sns.scatterplot(x = df['sepal_length'], y = df['sepal_width'])
plt.show()
"""

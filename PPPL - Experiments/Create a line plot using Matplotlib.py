# Create a line plot using Matplotlib to visualize trends over time in a dataset (e.g.,
# sales data, temperature changes, or stock prices). Include proper labels, titles, and
# legends for the plot.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\iu\Downloads\temp.csv")

df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

plt.figure(figsize=(10,6))
plt.plot(df['Year'], df['Average_Fahrenheit_Temperature'], label='Temperature (°F)', color='tab:blue')
plt.title('Average Temperature Over Years', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Temperature (°F)', fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()



"""
#Simple approach

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\IU\Downloads\temp.csv")

plt.plot(df['Year'], df['Average_Fahrenheit_Temperature'], label='Temp (°F)')
plt.show()

"""

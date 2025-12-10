import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('temp.csv')

print(data.head())

pie_chart = data.Rollno.plot(kind='pie')
plt.show()
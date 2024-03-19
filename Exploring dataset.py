import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.show()
data=pd.read_csv("telecom dataset.csv")
print(data)
print(data.head())
print(data.tail())
print(data.info())
print(data.shape())
print(data.nunique())
print(data.columns())
print(data.dtypes())
print(data.describe())
print(data.describe(include='object'))


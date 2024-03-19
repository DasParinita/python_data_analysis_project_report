import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.show()
data=pd.read_csv("telecom dataset.csv")
print(data.head(2))
print(data.isna().sum())
print(data.isnull().sum())
print(data.notnull().sum())
print(data.notna().sum())
print(data[data.duplicated()])
data=data.drop_duplicates()
print(data)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.show()
data=pd.read_csv("telecom dataset.csv")
print(data.head())
print(data['churn'].unique())
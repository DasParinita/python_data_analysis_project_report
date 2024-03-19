import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
data=pd.read_csv("telecom dataset.csv")
print(data.head())     #To show Top5 records of the dataset)
dc_pm = data['total day charge'].mean()/data['total day minutes'].mean()
# checking per minute day charge
ec_pm = data['total eve charge'].mean()/data['total eve minutes'].mean()
#checking per minute evening charge
nc_pm = data['total night charge'].mean()/data['total night minutes'].mean()
# checking per minute night charge
intc_pm = data['total intl charge'].mean()/data['total intl minutes'].mean()
# checking per minute international charge
sns.barplot(x=['day', 'evening', 'night', 'int'], y=[dc_pm, ec_pm, nc_pm, intc_pm])
plt.show()

# drawing a bar plot to represent different 'per minute call chagres
# Son x-axis we have given the naming... on y-axis we have given the charges 
#plt.show() to show the plot
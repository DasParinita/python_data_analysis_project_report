import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
data=pd.read_csv("telecom dataset.csv")
print(data.head())     #To show Top5 records of the dataset

# Ensure that the 'churn' column is of boolean type for proper handling in crosstab
data['churn'] = data['churn'].astype(bool)

# Computing a simple cross-tabulation of two columns, 'customer service calls' and 'churn'.
# 'margins=True' adds subtotals on rows and columns, giving us the total count as well.
cscalls = pd.crosstab(data['customer service calls'], data['churn'], margins=True)

# Creating a new column 'churn_percent' to show the percentage of churned customers
# against each count of customer service calls.
cscalls['churn_percent'] = cscalls[True] / cscalls['All'] * 100

print(cscalls)
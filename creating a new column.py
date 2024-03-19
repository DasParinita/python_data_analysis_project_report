import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the dataset

data = pd.read_csv("telecom dataset.csv")
veplan = pd.crosstab(data['voice mail plan'], data['churn'], margins = True)
veplan['churn percent'] = veplan [True] / veplan ['All'] * 100
print(veplan)

#creating a new coluen churn percent to show the churn percentage of the customers who were using voice mail plan
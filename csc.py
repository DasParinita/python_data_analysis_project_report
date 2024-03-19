import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_csv("telecom dataset.csv")
print(data['customer service calls'].nunique())
# To show the total number of nunique values present in column 'customer service calls'
print(data['customer service calls'].unique())
# To show the total number of unique values present in column 'customer service calls'
print(data['customer service calls'].value_counts())
# To show the count of the unique values of the column 'customer service calls from original dataframe
churn_data = data[data['churn']] #creating a new dataframe 'churn data", with the records of all churned customers
print(churn_data)

print(churn_data['customer service calls'].value_counts())
# To show the count/occurance of the unique values of the column 'customer service calls'
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
data=pd.read_csv("telecom dataset.csv")
print(data.head())     #To show Top5 records of the dataset

dc_pm = data['total day charge'].mean()/data['total day minutes'].mean()
# checking per minute day charge
ec_pm = data['total eve charge'].mean()/data['total eve minutes'].mean()
#checking per minute evening charge
nc_pm = data['total night charge'].mean()/data['total night minutes'].mean()
# checking per minute night charge
intc_pm = data['total intl charge'].mean()/data['total intl minutes'].mean()
# checking per minute international charge
print(dc_pm)  #prasting per minute day charge
print (ec_pm) #printing per minute evening charge
print(nc_pm) #printing per minute night charge
print(intc_pm) # printing per minute international charge
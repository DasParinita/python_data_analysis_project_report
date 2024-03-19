import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("telecom dataset.csv")
print(data.head(2)) # To show Top 2 records of the dataset
print(data.state.nunique())  # To show the total number of unique values present in column 'state'
print(data.state.unique())  # To show all the unique values of the column 'state'
# it shows the output in the form of 1-D array
print(data.state.value_counts()) #To show the occurance/count of all unique values of the columm "state"

#By default, it shows result in descending order
#To show the results in ascending order, we can write data.state.value_counts (ascending True)
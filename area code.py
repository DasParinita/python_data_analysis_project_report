import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv("telecom dataset.csv")
print(data.head())     #To show Top5 records of the dataset

   # nunique()
print(data['area code'].nunique())
#To show the total number of unique values present in the column 'area code

   # unique()
print(data['area code'].unique())
#To show all the unique values of the column 'area code... 
#it shows the output in the form of 1-0 array

    # value_counts()
print(data['area code'].value_counts())
#To show the occurance/count of all unique values of the column 'area code
# By default, it shows result in descending order
#To show the results in ascending order, we con write data, state. value counts (ascending True)

    # groupby()
print(data.groupby('area code') ['churn'].mean() * 100)
# Here, we will consider two columns while using groupby()
#Used groupby on 'area code" column and showing the mean of values of "chorn" column art to each area code... 
#...and multiplying the result by 100

    # crosstab()
# Calculatiog Area Code vs Churn Percentage
d = pd.crosstab(data['area code'], data['churn'], margins = True)
# using crosston function from panaasssorary to compute a simple ...
#...cross-tubulation of two columns le., 'area code' & 'churn and saving the output in varibate 'd'
# margins True means to show sum of both values in a new colume "ALL
d["Churn Percentage"]= d[True]/(d['All']) * 100
# Creating a new column 'Percantage Churn"....
# showing result of 'd'
# which shows the percentage of churn customers in each aned code
print(d)
  
        # countplot()
# Drawing a Bar Graph to show Area Code wise Churn
plt.figure(figsize=(14,5))
#Setting the size of the figure as 14x5, using matplotlib Library
sns.countplot(x = 'area code', hue = 'churn', data=data)
# Drawing a countplot for the column 'area code' from the dataset using seaborn Library....
#....selecting the Churn column for hue 
# ' hue = churn' represents that we want to use column 'churn for color encoding
# i.e. color the bars for Churn ant Not Chure differently
# Blue color representing Fulse (Not Churn) and Orange color representing True (Churn) for each area code separately
plt.show()  # To display the figure
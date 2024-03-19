import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv("telecom dataset.csv")
print(data.head())     #To show Top5 records of the dataset

    # nunique()
print(data['account length'].nunique()) # To show the total number of unique values present in the column 'account Length
      
      #creating dataframes()
#Creating two different dataframes one for 'churned customers' & second for 'non-churned customers'
churn_data = data[data['churn'] == True]
#creating a new dataframe "churn dota", in which we are considering all the records where churn is 'True'
not_churn_data = data[data['churn'] == False]
#creating a new dataframe "not churn data", in which we are considering all the records where charn is "False"

print(churn_data.head(2))    # To show Top2 records of the dataframe
print(not_churn_data.head(2))   #To show Top2 records of the dataframe

   #info()
print(churn_data.info())  #To show the basic information about the datafrose "churn_data"
#It shows indexes, columns counts, each column name with its non-mall values count & data-type, and memory of Dataframe
print(not_churn_data.info())  #To show the basic information about the dataframe "not churn data" 
#It shows indexes, columns counts, each column name with its non-null values count & data-type, and memory of Datoframe

   # shape
print(data.shape)
#To show the number of Rows & Columns in the DataFrame

      # Distribution Plot
# Creating a Distribution Plat for Account Length column
sns.kdeplot(data['account length'], color= 'orange') 
plt.xlabel("Account Length", fontsize=15)
plt.ylabel("Density", fontsize=15)
plt.show()
# The distplot shows a histogram with a line on it. It represents the distribution of a variable against the...
# ...density distribution
# Here, using Seaborn Library we are plotting a distribution plot for the column 'account length"....
#.....with "orange" color.
# Using matplotlib, setting the label of x-aris as "Account Length", with fontsize of 15
# Using matplotlib, setting the label of xaris as "Density", with fontsize of 15
# plt.show() To show the plot

import seaborn as sns
import matplotlib.pyplot as plt
# Assuming 'data', 'churn_data', and 'not_churn_data' are your DataFrame variables
# Plotting distribution of account length for all customers
sns.kdeplot(data['account length'], color='grey', label='All')
# Plotting distribution of account length for churned customers
sns.kdeplot(churn_data['account length'], color='red', label='Churned', linestyle="--")
# Plotting distribution of account length for not churned customers
sns.kdeplot(not_churn_data['account length'], color='yellow', label='Not Churned', linestyle=":")
# Setting labels and font sizes
plt.xlabel("Account Length", fontsize=15)
plt.ylabel("Density", fontsize=15)
# Setting the figure size
plt.rcParams['figure.figsize'] = (15, 7)
# Display the plot
plt.legend()  # Ensure the legend is shown
plt.show()

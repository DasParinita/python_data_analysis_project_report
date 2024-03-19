import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv("telecom dataset.csv")
print(data.head())   #To show Tops records of the dataset

     #unique()
print(data['international plan'].unique()) #To show all the unique values of the column 'international plan 
# #Two unique values present 'no' and 'yes

  #value counts()
print(data['international plan'].value_counts())
# To show the occurance/count of olt unique values of the colum 'International plan'
# By default, it shows result in descending order
# To show the results in ascending order, we can write data.state.value_count's(ascending True)

      #creating dataframe
# Creating a new datoframe 'yes int plan....
#.....containing the records of those Churned cus 2 customers who were having international plan
yes_int_plan = data[(data['international plan'] == 'yes') & (data['churn']==True)]
print(yes_int_plan)
# Here, we have used filtering with "8" operator, to select records satisfying two conditions
#1. 'international plan" -- "yes"
#2. 'churn'-- "True"
# It shows there are total 137 records satisfying these two conditions

# Creating a new dataframe 'no int plan....
#...containing the records of those Churned customers who don't have international plan
no_int_plan = data[(data['international plan'] =='no') & (data['churn']==True)]
print(no_int_plan)
#Here, we have used filtering with "&" operator, to select records satisfying the conditions
#1. "International plan"no"
#2. 'churn "True"
# it shows there are total 346 records satisfying these two conditions

# we noticed that 323 customers were using international plan, and 137 customers churned out of them 
# means a churn percentage of 42.4
print(137/323*100)

# we noticed that 3010 customers were not using lnternational plan, and 346 customers churned out of thes 
# means a churn percentage of 11.4
print(346/3010*100)

     # crosstab()
int_plan_data = pd.crosstab(data['international plan'], data['churn'], margins=True)
#Using crosstab function from pandas Library to compute a simple cross-tabulation... #...of two columns le., 'international plan" & "chure" and saving the output in varibule "int plan data margins True means to show the sum of both values in a new column "ALL"
print(int_plan_data)

      #Creating new column
#creating a new column "churn percent to show the churn percentage of the customers who were using international plan
int_plan_data['churn percent'] = int_plan_data[True]/int_plan_data['All']*100
print(int_plan_data)

      # info()
print(int_plan_data.info())   # To show the basic information about the datafrase "int_plan data"
#It shows indexes, columns counts, each column name with its non-nult values count & data-type, and memory of DataFrase
   
   
      #Value_counts()
i = data['international plan'].value_counts()
print(i)
#To show the count of the unique values of the column 'international plan', and saving in variable 'i'

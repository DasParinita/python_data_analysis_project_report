 # Showing Churn/Not Churn State-wise


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("telecom dataset.csv")

# Using seaborn Library, setting the background of the figure as "whitegrid"
sns.set(style="whitegrid")

# Setting the size of the figure as 20 x 7, using matplotlib Library
plt.figure(figsize=(20,7))

# Drawing a countplot for the column 'state' from the dataset using seaborn Library
# Selecting the 'churn' column for hue
# 'hue=data['churn']' represents that we want to use column 'churn' for color encoding
# i.e., color the bars for Churn and Not-Churn differently
# Blue color representing False (Not Churn) and Orange color representing True (Churn) for each state separately
sns.countplot(x='state', hue='churn', data=data)

# Setting the Label on x-axis as States, its fontsize & color
plt.xlabel('States', fontsize=18, color='DarkBlue')

# Setting the Label on y-axis as Count, its fontsize & color
plt.ylabel('Count', fontsize=18, color="DarkOrange")

plt.show()

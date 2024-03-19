import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("telecom dataset.csv")
print(data['number vmail messages'].value_counts().head()) #Showing the occurance/count of top 5 unique values of the column 'number vmail messages

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("telecom dataset.csv")

print(data['number vmail messages'].unique()) #To show the unique values present in the column 'number veoil messages


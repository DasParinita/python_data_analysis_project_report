import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the dataset

data = pd.read_csv("telecom dataset.csv")
u = data['voice mail plan'].unique()
print(u)
# To show all the unique values of the column 'voice  mail plan '
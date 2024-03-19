import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the dataset

data = pd.read_csv("telecom dataset.csv")
v = data['voice mail plan'].value_counts()
print(v)
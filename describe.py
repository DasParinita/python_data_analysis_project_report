import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("telecom dataset.csv")

print(data['number vmail messages'].describe())
# To check the summary statistics of the column. It checks extreme outliers and Large deviations etc.
# It shows the count of non-nult values, mean, std, minimus, maximum, 25th, 50th, 75th percentile value.
# Percentile means how many of the values are less than the given percentile.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_csv("telecom dataset.csv")
# Adjust the figure size
plt.figure(figsize=(5, 5))
# Creating a box plot
sns.boxplot(x='churn', y='number vmail messages', color='violet', showmeans=True, fliersize=5, meanprops={"marker":"o", "markerfacecolor":"white", "markeredgecolor":"black"}, data=data)
plt.show()  # To show the box plot

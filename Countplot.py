import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the dataset
data = pd.read_csv("telecom dataset.csv")
# Display the top records of the dataset
print(data.head())
# Set the figure size for the plot
plt.figure(figsize=(10, 5))
# Draw a countplot for the 'voice mail plan' column from the dataset,
# using the 'churn' column for hue to color-encode the Churn status
sns.countplot(x='voice mail plan', hue="churn", data=data,color='green')
# Show the plot
plt.show()

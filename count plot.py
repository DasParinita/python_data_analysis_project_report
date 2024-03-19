import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
data=pd.read_csv("telecom dataset.csv")
print(data.head())     #To show Top5 records of the dataset)
# Drawing a countplot for the column 'customer service calls' from the dataset using the Seaborn library.
# The 'churn' column is selected for hue to color the bars differently based on churn status.
# Set palette or color to differentiate between churned and not churned customers more effectively.
sns.countplot(x='customer service calls', hue='churn', data=data, palette="Set1")
# 'palette="Set1"' is used instead of a single color to automatically provide distinct colors for churned and not churned,
# making it clearer and avoiding the confusion of using the 'color' parameter, which would set all bars to the same color.
plt.title('Customer Service Calls and Churn')  # Adding a title to the plot
plt.xlabel('Number of Customer Service Calls')  # Labeling the x-axis
plt.ylabel('Count')  # Labeling the y-axis
plt.show()  # To display the plot

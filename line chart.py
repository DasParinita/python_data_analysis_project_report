import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("telecom dataset.csv")

a= data.groupby("state")['churn'].mean() * 100
# Sorting the results in ascending order
a.sort_values()

# Assuming 'data' is your DataFrame containing 'state' and 'churn' columns

# Setting the background style using seaborn
sns.set(style="whitegrid")

# Setting the size of the figure with matplotlib
plt.rcParams["figure.figsize"] = (20, 7)

# Getting all unique states
X = data['state'].unique()

# Calculating the mean churn rate for each state
Y = data.groupby("state")['churn'].mean() * 100

# Sorting Y by index to ensure the states are in alphabetical order for plotting
Y = Y.sort_index()

# It's important to also sort X in the same order as Y to match the states with their respective churn rates
X = sorted(X)

# Plotting the line chart
plt.plot(X, Y, color="black", marker='o', markersize=10)

# Setting the title and labels with specified font sizes
plt.title("State-Wise Churn Rate", fontsize=25)
plt.xlabel("State", fontsize=20)
plt.ylabel("Churn Rate (%)", fontsize=20)

# Rotating the state names on the x-axis for better readability
plt.xticks(rotation=90)

# Showing the plot
plt.show()

import matplotlib.pyplot as plt

# Assuming you have 'data' DataFrame containing 'state' and 'churn' columns

x = data.groupby("state")["churn"].mean().sort_values(ascending=False).head(5).index
y = data.groupby("state")["churn"].mean().sort_values(ascending=False).head(5).values + 100

plt.bar(x, y)
plt.xlabel('State')
plt.ylabel('Churn Rate')
plt.title('Top 5 States by Churn Rate (with +100)')
plt.show()

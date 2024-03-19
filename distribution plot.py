import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_csv("telecom dataset.csv")

# Use sns.histplot() for distribution plots
sns.histplot(data=data, x='number vmail messages', kde=True)

# Adding labels and title for clarity
plt.xlabel('Number of Voice Mail Messages')
plt.ylabel('Frequency')
plt.title('Distribution of Number of Voice Mail Messages')

plt.show()

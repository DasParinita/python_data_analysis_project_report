import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("telecom dataset.csv")
# Load the dataset
v = data['voice mail plan'].value_counts()
#Creating a Donut Chart of customers count 'having voice molt plan" and "not having voice mail plon'
plt.pie(v, labels=['No', 'Yes'], startangle=90, shadow = True, radius=1.5, explode=(0,0.1), autopct= '%1.2f%%')
circle = plt.Circle ((0,0),0.8, color='white')
c= plt.gcf()
c.gca().add_artist (circle)
plt.title("voice mail plan 051")
plt.show()

# Donut chart is a modified Pie chart, with an area from center cut out
#1 First, drawing a pie plot, using Matplotlib Library
# The dota is taken from the variable 'v'.... labels are given as 'No" & "Yes"
# startangle means the angle for slicing, set as 90...
# shadow is True means it will drop some shadow of the chart... radius of the circle is set as 1.5... 
#... explode is used to cut the slice out of the figure.....
# autopet is used to show the X on the chart upto recuired decimal points....
# 2 Second, using pit.Circle...we will create a circle and save it in the variable name 'eircle'...
# putting (0,0) by default... 0.8 is radius of circle and color of circle is 'white' 22#plt.gcf() is used to get the current figure.. and we are saving it in variable 'c'
# 3 Third, we will add the "circle" ot the center of oie chart... using gen() add artist()
# We have given the title to the chact using plt.title() 
# plt.show() To show the chart
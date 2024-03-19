import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv("telecom dataset.csv")
i = data['international plan'].value_counts()
# Creating a Donut Chart of customers count 'having international plan' and 'not having international plan

plt.pie(i, labels=['No', 'Yes'], colors=['yellow', 'Cyan'], startangle=50, shadow=True, radius=2, 
        explode= (0,0.2), autopct= '%1.2f%%', pctdistance=0.75);

circle = plt.Circle((0,0), 1, color='white') 
c= plt.gcf()
c.gca().add_artist (circle) 
plt.title("International Plan (DSL)")
plt.rcParams['figure.figsize'] = (5,7)
plt.show()
# Donut chart is a modified Pie chart, with an area from center cut out
# 1 First, drawing a pie plot, using Natplotlib Library
# The data is taken from the variable i labels are given as 'No' & 'Yes"...
# .... color is given to each label 'yellow' & 'cyan startangle means the angle for slicing, set as 50 ...
# ..... shadow is True means it will drop some shadow of the chart... rodius of the circle is set as 2
# ...... explode is used to cut the slice out of the figure
#..... autopct is used to show the $ on the chart upto required decimal points...
# .... pctdistance is given for distance of X from the center
# 2 Second, using plt.Circle...we will create a circle and save it in the variable name "circle"...
# ... putting (0,0) by default... 1 is radius of circle... and color of circle is 'white'
# plt.gcf() is used to get the current figure... and we are saving it in variable 'c 26 #3 Third, we will add the 'circle' at the center of ple chart.. using gea().add_artist()
# We have given the title to the chart using plt.title()
# Using reparans from matplotlib Library, setting the size of the figure as 5x7
# plt.show() To show the chart
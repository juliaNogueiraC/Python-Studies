# the pie() function to creat a pie chart
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 
#------------------------------
# add labels
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)

#-------------------------
# stand out a piece of the pie
# use the "explode" parameter
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
# this number show so far is the piece from the center of the pie 

plt.pie(y, labels = mylabels, explode = myexplode)


#---------------------------
#shadow
plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)

#-------------------------
# colors
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)

#-----------------------
# legend 
# use the functio legend()
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show() 

# legend with header:
plt.legend(title = "Four Fruits:")

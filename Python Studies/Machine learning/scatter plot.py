#A scatter plot is a diagram where each value in the data set is represented by a dot.

#The Matplotlib module has a method for drawing scatter plots, it needs two arrays of the same length, one for the values of the x-axis, and one for the values of the y-axis:
import Matplotlib as plt
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#The x array represents the age of each car.

#The y array represents the speed of each car.

plt.scatter(x, y)
plt.show()

#-------------------------
# random data distributions
import numpy
import Matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()
#We can see that the dots are concentrated around the value 5 on the x-axis, and 10 on the y-axis.
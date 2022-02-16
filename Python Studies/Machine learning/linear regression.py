#In Machine Learning, and in statistical modeling, that relationship is used to predict the outcome of future events.
#Import scipy and draw the line of Linear Regression:

import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

#----------------------------------
# Predict future values
#Let us try to predict the speed of a 10 years old car.
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

speed = myfunc(10)

print(speed)

#-----------------------------------
#R for Relationship
#It is important to know how the relationship between the values of the x-axis and the values of the y-axis is, if there are no relationship the linear regression can not be used to predict anything.

#This relationship - the coefficient of correlation - is called r.

#The r value ranges from -1 to 1, where 0 means no relationship, and 1 (and -1) means 100% related.

#How well does my data fit in a linear regression?

from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)


#Note: The result -0.76 shows that there is a relationship, not perfect, but it indicates that we could use linear regression in future predictions.
#------------------------------
#R-Squared
#It is important to know how well the relationship between the values of the x- and y-axis is, if there are no relationship the polynomial regression can not be used to predict anything.

#The relationship is measured with a value called the r-squared.

#The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.

#how well does my data fit in a polynomial regression?

import numpy
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))

#Note: The result 0.94 shows that there is a very good relationship, and we can use polynomial regression in future predictions.

#----------------------------------
# predict future values
#Example: Let us try to predict the speed of a car that passes the tollbooth at around 17 P.M:

import numpy
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

speed = mymodel(17)
print(speed)
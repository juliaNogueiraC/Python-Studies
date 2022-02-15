#In this chapter we will learn how to create an array where the values are concentrated around a given value.
import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()

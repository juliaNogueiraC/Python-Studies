#use the bar() function to draw bars
#Draw 4 bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

#----------------------------
#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

x = ["APPLES", "BANANAS"]
y = [400, 350]

plt.bar(x, y)
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()


#--------------------------
# horizontal bars
# barh()
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()

#----------------------------------
# the bar color
plt.bar(x, y, color = "red")

plt.bar(x, y, color = "#4CAF50")

#---------------------------
# bar widht 
plt.bar(x, y, width = 0.1)
#Note: For horizontal bars, use height instead of width.
#---------------------------------
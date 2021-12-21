# global variable. Variables that are created outside of a function (as in all of the examples above) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.
def myfunc():
  
  global x
  x = "fantastic"

#another example of global variable 

x = "awesome"

def myfunc2():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#----------------------------------------------
# show the variable type

x = "Hello World"
print(type(x))

#If you want to specify the data type of a variable, this can be done with casting. Example:

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#----------------------------------------------
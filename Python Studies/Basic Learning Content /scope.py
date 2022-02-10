#A variable is only available from inside the region it is created. This is called scope.



#If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = 300

myfunc()

print(x)
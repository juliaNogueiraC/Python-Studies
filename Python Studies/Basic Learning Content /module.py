#Consider a module to be the same as a code library. A file containing a set of functions you want to include in your application.


# CREATING A MODULE
# create a file, and " import thisFile" in another file 
 #thifFile.py
 def greeting(name):
  print("Hello, " + name)

  #anotherFile.py
  import mymodule

mymodule.greeting("Jonathan")
#-----------------------------
# VARIABLES IN MODULE 
# module.py
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#anotherFile.py 
import module

a = module.person1["age"]
print(a)
#--------------------------------
# the dir() function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

#Example: List all the defined names belonging to the platform module:

import platform

x = dir(platform)
print(x)




#----------------------
#You can choose to import only parts from a module, by using the from keyword.
from mymodule import person1

print (person1["age"])


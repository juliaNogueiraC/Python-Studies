# Function is a block of code which only runs when it is called


# creating a function
def my_function():
  print("hi")


#calling a function:
def my_function():
  print("hi")

my_function()
#---------------------------------

#Arguments
# the informations can be passed into functions as arguments

def my_function(fname):
  print(fname + "refsnes")

my_function("emile")
my_function("peter")


# difference between parameters or arguments: parameter is the variable listed inside the parentheses in the fuction definition. an argument is the value that is sent to the function when it is called. 

# 2 arg
def function(name, lastname):
  print(name + " " + lastname)

function("peter", "feio")

#----------------------------------
# arbitrary args 
# if you dunno how many args will be passed, add * before the parameter name

def function1(*kids):
  print("the first child is" + kids[0])

function1("peter", "maria")

#----------------------------------
#keyword args
# you can send args using the key = value syntax. the order of the args does not matter.
def function2(kid3, kid2, kid1):
  print(" the first kid " + kid1)

function1(kid1 = "peter", kid2 = "lucas", kid3 = "john")


#-------------------------------
#arbitrary keyword args, **kwargs 
# add ** before the parameter name if you dunno how many keyword args that will be passed into function.

def function3(**kid):
  print(" the first kid is " +kid["kid1"])

function3(kid1 = "peter", kid2 = "lucas")


#-------------------
# Default parameter value 
#if u call a functions without arg, it uses a default value
def function3(country = "Japan"):
  print("i'm from" + country)

function3("Brazil")


#--------------
#passing a list as an args
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


#---------------------
#return a value

def mult(x):
  return 1000 * x

print(mult(9))
print(mult(1))

#-----------------
# recursion....
# functions which calls itself 

def rec(x):
  if(x > 0):
    r = x + rec(x-1)
    print(r)

  else:
    r = 0
  return r 


print("\n\n results")
rec(2)

# other example of recursion 

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))

#explaining...
#factorial(3)          # 1st call with 3
#3 * factorial(2)      # 2nd call with 2
#3 * 2 * factorial(1)  # 3rd call with 1
#3 * 2 * 1             # return from 3rd call as number=1
#3 * 2                 # return from 2nd call
#6                     # return from 1st call


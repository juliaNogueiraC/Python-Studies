# it is a small anonymous function . it can take any number of args, but it can only have one expression

# lambda arguments : expression 

#example:
x = lambda A : A + 1000
print(x(90))

#more 
x = lambda b, c : b * c 
print(x(10.10))


# examples 

def myfunc(n):
  return lambda a : a - n

mydoubler = myfunc(2)

print(mydoubler(11))
# the A will be 11 and the n will be 2 

# more...
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))
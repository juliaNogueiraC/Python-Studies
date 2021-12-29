# creating a class...
class Cars:
  def __init__(self, m, p):
    self.model = m
    self.price = p
 
Audi = Cars("R8", 100000)
 
print(Audi.model)
print(Audi.price)

#---------------------------------
# the _init_() Function 
# all class have a function int, which is executed when the class is being initiated 
# use this function to assign value to object properties, of any operation that is ncessary to do when the object is being created 

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#----------------------
#Object methods 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#-------------------------------------------
# the self parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

#It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#-------------------
#modify object properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age)


#--------------------------------
# delete object properties 

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age

print(p1.age) # it will have erro because it was deleted 

#------------------------
# delete objects 

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1

print(p1) # it will have erro because you deleted it 

#--------------------------------
# pass statement 
#class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class Person:
  pass

# having an empty class definition like this, would raise an error without the pass statement




#----------------------------------
# Python program to create instance
# variables inside methods
	
class Car:
		
	# Class Variable
	vehicle = 'car'
		
	# The init method or constructor
	def __init__(self, model):
			
		# Instance Variable
		self.model = model			
	
	# Adds an instance variable
	def setprice(self, price):
		self.price = price
		
	# Retrieves instance variable	
	def getprice(self):	
		return self.price	
	
# Driver Code
Audi = Car("R8")
Audi.setprice(1000000)
print(Audi.getprice())


#-------------
# another example 
class Car:
	
	# Class Variable
	vehicle = 'Car'		
	
	# The init method or constructor
	def __init__(self, model, price):
	
		# Instance Variable	
		self.model = model
		self.price = price		
	
# Objects of class
Audi = Car("R8", 100000)
BMW = Car("I8", 10000000)

print('Audi details:')
print('Audi is a', Audi.vehicle)
print('Model: ', Audi.model)
print('price: ', Audi.price)

print('\n BMW details:')
print('BMW is a', BMW.vehicle)
print('Model: ', BMW.model)
print('Color: ', BMW.price)

# Class variables can be
# accessed using class
# name also
print("\nAccessing class variable using class name")
print(Car.audi)		

#a-----------------
#another 
class Test:
def __init__(Myobject, a, b):
	Myobject.country = a
	Myobject.capital = b

def myfunc(abc):
	print("Capital of " + abc.country +" is:"+abc.capital)

x = Test("India", "Delhi")
x.myfunc()

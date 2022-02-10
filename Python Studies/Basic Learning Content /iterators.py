# INTERATORS:
#An iterator is an object that contains a countable number of values.
#Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

#INTERATOR VS INTERABLE
#Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
#All these objects have a iter() method which is used to get an iterator
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#Even strings are iterable objects, and can return an iterator
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#-------------------------------
# lOOPING THROUGH AN INTERATOR
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

#----------------------------------
# creating an INTERATOR
#To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#---------------------------------
# StopIteration
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

#-------------------------------


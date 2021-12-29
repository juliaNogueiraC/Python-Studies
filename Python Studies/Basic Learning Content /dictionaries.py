#Use the get method to print the value of the "model" key of the car dictionary.


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#----------------------------------------------

#Change the "year" value from 1964 to 2020.


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#----------------------------------------------
#Add the key/value pair "color" : "red" to the car dictionary.


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
#----------------------------------------------
#Use the pop method to remove "model" from the car dictionary.


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
#----------------------------------------------

#Use the clear method to empty the car dictionary.


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#----------------------------------------------
#ways to print the dictionary
fruits = {
"cor": "preto",
"texture": "fino!",
"sla": "sslaa"

}
print(fruits)
# or:
for key,value in fruits.items():
	print(key, ':', value)
#or:
for key in fruits.keys():
	print(key)
#or:
for value in fruits.values():
	print(value)


#----------------------------------------------
# acessing items...
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#or 
x = thisdict.get("model")  

#The keys() method will return a list of all the keys in the dictionary.

x = thisdict.keys() 


#The values() method will return a list of all the values in the dictionary.
x = thisdict.values()

# the items() will return each item in a dictionary 
x = thisdict.items()

#----------------------------------------------
#CHECK IF KEY EXISTS 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": "1964"
}

if "model" in thisdict: 
  print(" yes, there is 'model'.")

  
#----------------------------------------------
# UPDATE
#Update the "year" of the car by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#----------------------------------------------
#REMOVING 
#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)


#The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#The del keyword can also delete the dictionary completely:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict


#----------------------------------------------
#LOOP
for x in thisdict:
  print(x)


#print  all values in the dictionary, one by one

for x in the thisdict:
  print(thisdict[x])

#You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
  print(x)

#You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
  print(x)

#Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)


#----------------------------------------------
# COPY 
#Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


#Make a copy of a dictionary with the dict() function:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#----------------------------------------------
# NESTED DIC

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


#----------------------------------------------

#METHODS
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
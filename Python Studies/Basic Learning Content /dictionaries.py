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
  
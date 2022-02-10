# JSON is a syntax for storing and exchanging data. it is a text made using JS object notation
#importing the json module:
import json

#If you have a JSON string, you can parse it by using the json.loads() method. it will turn a dictionary 

import json
x = '{ "name": "peter", "age":30, "city":"TOKYO"}'

y = json.loads(x)

print(y)
print(y["age"])

#---------------------------------------------------------------------
#If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
import json

 x = {
   "name": "Peter",
   "age": 10,
   "city": "TOKYO"

 }

 y = json.dumps(x)
 print(y)


#-----------------------------------------------------------------------
#Convert Python objects into JSON strings, and print the values:

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))



#Python ---JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null

#------------

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))


#Use the sort_keys parameter to specify if the result should be sorted or not:

json.dumps(x, indent=4, sort_keys=True)






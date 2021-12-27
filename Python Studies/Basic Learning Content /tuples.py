#Use the correct syntax to print the first item in the fruits tuple.


fruits = ("apple", "banana", "cherry")
print(fruits[0])

#----------------------------------------------
#Use the correct syntax to print the number of items in the fruits tuple.


fruits = ("apple", "banana", "cherry")
print(len(fruits))

#----------------------------------------------
#Use negative indexing to print the last item in the tuple.


fruits = ("apple", "banana", "cherry")
print(fruits[-1])
#----------------------------------------------

#Use a range of indexes to print the third, fourth, and fifth item in the tuple.


fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#----------------------------------------------
# tuple as constructor: Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#----------------------------------------------
#Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


#----------------------------------------------
#Change Tuple Values
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#----------------------------------------------
#Add Items
#Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.

#----------------------------------------------
#REMOVE ITEMS 
#Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

#Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
#----------------------------------------------
#Using Asterisk
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#----------------------------------------------
# LOOP TUPLES
#Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Print all items by referring to their index number:

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#Print all items, using a while loop to go through all the index numbers:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


#----------------------------------------------
#Methods

count()	#Returns the number of times a specified value occurs in a tuple


index()#	Searches the tuple for a specified value and returns the position of where it was found



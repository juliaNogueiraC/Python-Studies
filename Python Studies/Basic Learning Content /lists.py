#Print the second item in the fruits list.


fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#----------------------------------------------

#Change the value from "apple" to "kiwi", in the fruits list.


fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
#----------------------------------------------

#Use the append method to add "orange" to the fruits list.


fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
#----------------------------------------------

#Use the insert method to add "lemon" as the second item in the fruits list.


fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
#----------------------------------------------

#Use the remove method to remove "banana" from the fruits list.


fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#----------------------------------------------
#Use negative indexing to print the last item in the list.


fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#----------------------------------------------
#se a range of indexes to print the third, fourth, and fifth item in the list.


fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#----------------------------------------------

#Use the correct syntax to print the number of items in the list.


fruits = ["apple", "banana", "cherry"]
print(len(fruits))
#----------------------------------------------
#Print List
fruits = ["apple", "banana", "melon", "lemon", "avocado"]


newfruit = input()
fruits.append(newfruit)

for x in range(len(fruits)):
 print(fruits[x])

# without using loop
  
a = [1, 2, 3, 4, 5]
  
# printing the list using * operator separated 
# by space 
print(*a)
  
# printing the list using * and sep operator
print("printing lists separated by commas")
  
print(*a, sep = ", ") 
  
# print in new line
print("printing lists in new line")
  
print(*a, sep = "\n")


#----------------------------------------------
#Convert a list to a string for display : If it is a list of strings we can simply join them using join() function, but if the list contains integers then convert it into string and then use join() function to join them to a string and print the string.
# Python program to print list
# by Converting a list to a 
# string for display
a =["Geeks", "for", "Geeks"]
  
# print the list using join function()
print(' '.join(a))
  
# print the list by converting a list of 
# integers to string 
a = [1, 2, 3, 4, 5]
  
print str(a)[1:-1] 

#----------------------------------------------
# Python program to print list
# print the list by converting a list of 
# integers to string using map
  
a = [1, 2, 3, 4, 5]
print(' '.join(map(str, a))) 
  
print"in new line"
print('\n'.join(map(str, a)))

#----------------------------------------------
#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#----------------------------------------------

#Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#----------------------------------------------

#Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#----------------------------------------------
#Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#----------------------------------------------
#Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#----------------------------------------------
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

#Example :Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#----------------------------------------------

#The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index. if you dont define the index, this method will remove the item

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#The del keyword also removes the specified index. but it also can delete the entire list
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)



# the clear method will empty the entire list 
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#----------------------------------------------
# LOOP LISTS 
#Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


#A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#----------------------------------------------
# LIST COMPREHENSION 
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#Example:Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# with comprehension:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


#----------------------------------------------
#List Alphanumerically
#Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#----------------------------------------------
# COPY LISTS
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#or:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#----------------------------------------------
# Join Lists
# simple way: 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#another way, most interesting, appending all the items from list2 into list1, one by one:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#another way.... thsi way add the list2 at the end of list1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#----------------------------------------------
#LIST METHODS
append() #	Adds an element at the end of the list

clear()	#Removes all the elements from the list

copy()	#Returns a copy of the list

count()	#Returns the number of elements with the specified value

extend() #	Add the elements of a list (or any iterable), to the end of the current list

index()#	Returns the index of the first element with the specified value

insert()	#Adds an element at the specified position

pop()	#Removes the element at the specified position

remove()#	Removes the item with the specified value

reverse()#	Reverses the order of the list

sort()	#Sorts the list

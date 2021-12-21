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


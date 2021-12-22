#Use the len method to print the length of the string.


x = "Hello World" 
print(len(x))

#----------------------------------------------
#Get the first character of the string txt.

txt = "Hello World"
x = txt[0]

#----------------------------------------------
#Get the characters from index 2 to index 4 (llo).

txt = "Hello World"
x = txt[2:5]
#----------------------------------------------

#Return the string without any whitespace at the beginning or the end.

txt = " Hello World "
x = txt.strip()
#----------------------------------------------
#Convert the value of txt to upper case.


txt = "Hello World"
txt = txt.upper()

#----------------------------------------------
#Convert the value of txt to lower case.


txt = "Hello World"
txt = txt.lower()
#----------------------------------------------
#Replace the character H with a J.


txt = "Hello World"
txt = txt.replace("H", "J")

#----------------------------------------------
#Insert the correct syntax to add a placeholder for the age parameter.


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#----------------------------------------------
#Looping Through a String
for x in "banana":
  print(x)

#----------------------------------------------
# Check String
#Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)
#Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#----------------------------------------------
#Check if NOT
#Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)
#Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


#----------------------------------------------
# Slicing strings: 
#Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

#Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])

#Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])


#----------------------------------------------
#Modify strings
#The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())

#The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())

#The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#----------------------------------------------
#Concatenation
#Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)

#To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#----------------------------------------------
#Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#----------------------------------------------
# STRING METHODS
capitalize() #	Converts the first character to upper case

casefold() #	Converts string into lower case

center() #	Returns a centered string

count()	#Returns the number of times a specified value occurs in a string

encode() #	Returns an encoded version of the string

endswith() #	Returns true if the string ends with the specified value

expandtabs() #	Sets the tab size of the string

find()	#Searches the string for a specified value and returns the position of where it was found

format() #	Formats specified values in a string

format_map()	#Formats specified values in a string

index()	#Searches the string for a specified value and returns the position of where it was found

isalnum() #	Returns True if all characters in the string are alphanumeric

isalpha()	#Returns True if all characters in the string are in the alphabet

isdecimal()	#Returns True if all characters in the string are decimals

isdigit() #	Returns True if all characters in the string are digits

isidentifier()	#Returns True if the string is an identifier

islower() #	Returns True if all characters in the string are lower case

isnumeric()	#Returns True if all characters in the string are numeric

isprintable()	#Returns True if all characters in the string are printable

isspace()#Returns True if all characters in the string are whitespaces

istitle() #	Returns True if the string follows the rules of a title

isupper()	#Returns True if all characters in the string are upper case

join() #	Joins the elements of an iterable to the end of the string

ljust()#	Returns a left justified version of the string

lower()	#Converts a string into lower case

lstrip() #	Returns a left trim version of the string

maketrans() #	Returns a translation table to be used in translations

partition()	#Returns a tuple where the string is parted into three parts

replace()	#Returns a string where a specified value is replaced with a specified value

rfind()	# Searches the string for a specified value and returns the last position of where it was found

rindex()	#Searches the string for a specified value and returns the last position of where it was found

rjust()	#Returns a right justified version of the string

rpartition() #	Returns a tuple where the string is parted into three parts

rsplit()#Splits the string at the specified separator, and returns a list

rstrip()	#Returns a right trim version of the string

split()	#Splits the string at the specified separator, and returns a list

splitlines()	#Splits the string at line breaks and returns a list

startswith()#	Returns true if the string starts with the specified value

strip()#Returns a trimmed version of the string

swapcase()#	Swaps cases, lower case becomes upper case and vice versa

title()	#Converts the first character of each word to upper case

translate()#	Returns a translated string

upper()	#Converts a string into upper case

zfill()	# Fills the string with a specified number of 0 values at the beginning
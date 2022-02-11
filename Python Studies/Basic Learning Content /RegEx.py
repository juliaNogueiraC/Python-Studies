# REGULAR EXPRESSSIONS: this is a sequence of characters that forms a search pattern. it can be used to check if a string contains the specified pattern

# REGEX MODULE
import re

#-------------------------------------------------------

# example 
import re
#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

#--------------------------------------------------
#RegEx FUNCTIONS
Function ----	Description
findall   	Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	      Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string

#----------------------------------------------------
# the findall() Function

import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#-----------------------------------------------
#the search() Function
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 
#-------------------------------------------------
# the spliy() Function
import re

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#You can control the number of occurrences by specifying the maxsplit parameter:
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

#---------------------------------------------------
# the sub() Function
import re

#Replace all white-space characters with the digit "9":

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

#----------------------------------------------------
#The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match


#Print the position (start- and end-position) of the first match occurrence.

#The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


#another...

import re

#The string property returns the search string:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

# another
import re

#Search for an upper case "S" character in the beginning of a word, and print the word:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

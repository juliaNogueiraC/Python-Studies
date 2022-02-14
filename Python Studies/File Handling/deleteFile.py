#Remove the file "demofile.txt":

import os
os.remove("demofile.txt")

#Check if file exists, then delete it:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#To delete an entire folder, use the os.rmdir() method:
import os
os.rmdir("fileName")
#Note: You can only remove empty folders.

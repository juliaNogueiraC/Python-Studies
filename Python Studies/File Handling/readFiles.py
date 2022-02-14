f = open("demofile.txt", "r")
print(f.read())

#If the file is located in a different location, you will have to specify the file path, like this:

f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

# the read() returns the whole text but u can specify hoe many characters to return 

f = open("fileName.txt", "r")
print(f.read(5))


#read lines
f = open("demofile.txt", "r")
print(f.readline())
#calling readline() two times, you can read the two first lines:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
#By looping through the lines of the file, you can read the whole file, line by line:
f = open("demofile.txt", "r")
for x in f:
  print(x)


#close files 
f = open("demofile.txt", "r")
print(f.readline())
f.close()


import os
#do I need to use glob?


#currentDirectory = os.getcwd() #not just on my desktop
#nevermind the above I can just use "."


image_list = open("output.txt","w+")

for path, subdirs, files in os.walk("."):
    for x in files:
        if x.endswith(".jpg"):
            image_list.write(os.path.join(path, x) + ", " + str(path) +"\n") #testing path
        if x.endswith(".png"):
            image_list.write(os.path.join(path, x) + ", " + str(path) +"\n") #testing path

image_list.close()

with open("output.txt","r") as print_list: #so I can look at it in console
	print (print_list.read())
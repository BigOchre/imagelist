
import os
#do I need to use glob?


#currentDirectory = os.getcwd() #not just on my desktop
#nevermind the above I can just use "."


image_list = open("output.txt","w+")

for path, subdirs, files in os.walk("."):
    for x in files:
        if x.endswith(".jpg"):
            image_list.write(os.path.join(path, x) +"\n")
        if x.endswith(".png"):
            image_list.write(os.path.join(path, x) + "\n")
image_list.close()
image_list = open("output.txt","r")
print (image_list.read())
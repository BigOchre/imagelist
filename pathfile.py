
import os
#do I need to use glob?


#currentDirectory = os.getcwd() #not just on my desktop
#nevermind the above I can just use "."


image_list = open("output.csv","w+")

for path, subdirs, files in os.walk("."):
    for x in files:
        if x.endswith(".jpg"):
            image_list.write(os.path.join(path, x) + ",") 
            path_sans_point = str(path).replace(".","") #get rid of point
            new_point = path_sans_point.replace("\\","") #get rid of slash in pathname
            image_list.write(new_point +"\n")

        if x.endswith(".png"):
            image_list.write(os.path.join(path, x) + ",")
            path_sans_point = str(path).replace(".","")
            new_point = path_sans_point.replace("\\","")
            image_list.write(new_point +"\n")


image_list.close()

with open("output.csv","r") as print_list: #so I can look at it in console
	print (print_list.read())


#You can use open method to open a file as:
file = open("my_file.txt")   #Opens a file and returns file object and stores 
                             #it in file variable which is now an object

contents = file.read()       #This returns the contents of file as string and stores it in variable contents
print(contents)
file.close()                 #Close after opening



#There is different way of opening a file that is more preferred over above way
with open("my_file.txt") as file:
    contents = file.read()       
    print(contents)
#In this method we dont have to close the file it is managed by with


#If we want to write into file we can do so as:
with open("my_file.txt", mode = "w") as file:      #By default the file opens as read only so to write 
                                                   #we have to specify the mode. We used keyword argument.
    file.write("I Love to Code!")                  #This is write so it overwrites the entire file

#Only in write "w" mode if the file dosent exist it creates a new one for us

#if we want to append instead of write:
with open("my_file.txt", mode = "a") as file:                                                     
    file.write("\nI Love to Code!")    #\n for new line    


#Note the above file path works only because we are on same level as it otherwise use diff file path






#Some errors might be:
# Opening a non-existing File 
# Trying to access key that dosent exist from a dictionay
# Using invalid opeations on a data type


#We can catch these exceptions using exception handling 
# try: something that might cause an Exception 
# except: do this if there was an exception
# else: do this if there were no exceptions
# finally: do this no matter what

try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["kkjcb"])
except FileNotFoundError:    #It is recommended to specify what type of error is it handling although you can use naked except
    file = open("a_file.txt","w")
    file.write("Something")         
except KeyError as error_message:          #We can also get hold of the error message
    print(f"That key {error_message} dosent exist")

else:
    content = file.read()    
    print(content)      #If we have no error these are executed

finally:
    file.close()
    print("File was closed")   #Even if it raises exception we close the file

#You can raise your own exceptions using raise


#If you have an empty function or class which you want to work on later then you can use pass keyword to not get an error

# class User:
#     pass

#Class is named in Pascal Case

#Types of case:
#PascalCase
#camelCase
#snake_case



#You can create attribute by:
class Car:
    pass

my_car = Car()

my_car.name = "Audi"        #Creates an attribute
print(my_car.name)






#But this method is prone to error so we use constructor which is an especial function that initializes the
#values of attributes when an object is initialized/constructed

class Student:
    def __init__(self,roll,name):    #This init function is the constructor that initializes the attributes of the object
        self.roll = roll             #This init function gets triggered everytime a new object is created
        self.name = name             #self is similar to this in cpp and must be the first parameter
                                     #which represents current object of class 
                                     #Name of attribute dosent necessarily have to be the same as the name of parameter passed but it is the convention

#Now we can easily construct objects as:
student1 = Student(5,"Jack")


#We can also have default values for some attributes and not pass them while constructing e.g:

class User:
    def __init__(self):
        self.followers = 0

user1 = User()
print(user1.followers)             #This will print 0 











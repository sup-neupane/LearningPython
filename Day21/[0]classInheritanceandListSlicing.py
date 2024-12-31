#We can inherit both methods and attributes from a class 
#e.g:
class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, Exlahle.")


class Fish(Animal):             #Fish wants to inherit from Animal class
    def __init__(self):
        super().__init__()        #super refers to the super class i.e. Animal so this line initializes everything our Animal class
                                  #can do inside Fish class both methods and attribute
    def swim(self):
        print("Moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()       #Nemo can now do both these methods
print(nemo.num_eyes) #Nemo can also have the attribute



#What if we want to do something extra with method after inheriting we can do so by:
class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, Exlahle.")


class Fish(Animal):             
    def __init__(self):
        super().__init__() 

    def breathe(self):
        super().breathe()              #Do everything breathe in Animal does
        print("Doing this underwater") #Also do this

    def swim(self):
        print("Moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()       
print(nemo.num_eyes) 

#We can slice a list and extract freagments as:
my_list = ["a","b","c","d","e","f","g"]
print(my_list[2:5])       #Prints c d and e as 2:5 gets element 2 to 4 (mind index 0)
print(my_list[2:])        #This slices from 2 so a b is cut out rest are retained
print(my_list[:2])        #This slices from 2 so a b is retained others are cut
print(my_list[2:5:2])     #The last number gives increment in which the values are retained so it prints c and e
print(my_list[::2])       #This prints every other items in list i.e. a c e g
print(my_list[::-1])      #This reverses the list

#All these above operations also works for tuples



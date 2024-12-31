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





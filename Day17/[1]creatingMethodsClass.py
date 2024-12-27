#We can also have methods (functions attached to class) a method must have self as first pointer
class User:
    def __init__(self,name):
        self.name = name 
        self.followers = 0
    
    def increaseFollowers(self):
        self.followers += 1


user1 =  User("Suparna")       #Create user1 object with name as "Suparna" and followers 0 as default
print(user1.followers)         #This prints 0
user1.increaseFollowers()      #Increase followers
print(user1.followers)         #This prints 1

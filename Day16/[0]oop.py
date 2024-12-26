#In OOP we model real life objects and these objects have attributes and methods
#These objects are generated from blueprint called class
# e.g. car = CarBlueprint() this is how we can construct/instantiate object car from class CarBlueprint
import turtle

timmy = turtle.Turtle()

# Here timmy is an object of class Turtle which is inside turtle module


# Easier way might be:
# from turtle import Turtle
# timmy = Turtle()

#We can use . operator to access the attributes and methods/functions of the object
#Say we create my_screen object from Screen class from turtle module 
my_screen = turtle.Screen()
print(my_screen.canvheight)   #This allows us to access the attribute canvheight 

my_screen.exitonclick()    #This allows us to access exit on click method defined in class for object my_screen and 
                           #solves our problem of sceen disppearing



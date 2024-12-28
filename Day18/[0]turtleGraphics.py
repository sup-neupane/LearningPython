from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()     #Make new object timmy_the_turtle
timmy_the_turtle.shape("turtle")   #Set shape of timmy to turtle
timmy_the_turtle.color("red")   #Set color of turtle to red


 #Making a square
# for _ in range(4):
#     timmy_the_turtle.forward(100)   #Move turtle 100 steps
#     timmy_the_turtle.right(90)


#Making dashed line
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()          #Pulls up pen
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()  


#Drawing shapes
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for number_of_sides in range(num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

for shape_sides_n in range(3,11):
    timmy_the_turtle.color(random.choice(colours))
    draw_shape(shape_sides_n)





#Create screen and make it so that it only exits on click this must be at end of code
screen = Screen()
screen.exitonclick()



#Ways to import
# import module_name
# from package_name import thing_from_module
# from package_name import *    #This imports everything from a module
# import module_name as alias_name   #You can use alias name to access the module
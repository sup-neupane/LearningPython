# Tules are data type that looks like (1,2,3)
#It is similar to a list in a sense it is ordered
my_tuple = (1,2,3)
print(my_tuple[0])   #This prints 1

#But is different as we cannot reaasign its value to sth else
# my_tuple[0] = 0         #This will throw an error

#You can convert a tuple to list by:
# list(tuple name)
#Tuples are used for things that dont change


#Random walk using tuples
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r =  random.randint(0,255)
    g =  random.randint(0,255)
    b =  random.randint(0,255) 
    color = (r,g,b)
    return color


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()

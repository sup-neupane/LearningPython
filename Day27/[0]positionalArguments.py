#We have covered positional and keyword arguments
#We can also have default arguments for a fuction
def simple_interest(p =1000 ,t =2,r=1.5):
    return (p * t * r) / 100

#SI with default arguments:
print(simple_interest())

# With value for t but others default:
print(simple_interest(t=5))

#We can also provide unlimited arguments by using *args
#*is required but args is convention use can use any other
#Once inside function you can loop through args e.g:

def sum(*args):
    sum = 0
    for number in args:   #args is tuple
        sum += number
    return sum

#You can now sum 2 numbers as:
print(sum(2,3))

#You can now sum 3 numbers as:
print(sum(2,3,4))

#Also called Many positional arguments as it creates a tuple and order in tuple matters

#Now as *args creates a tuple of arguments we have to fix position
#If we want to create many positional arguments we use **kwargs

def calculate(**kwargs):
    print(kwargs)
    print(kwargs["add"])     #This prints 3. We can now do anything with the value using keys

calculate(add = 3, multiply = 5)
#**kwargs converts these to dictionary  {'add': 3, 'multiply': 5}




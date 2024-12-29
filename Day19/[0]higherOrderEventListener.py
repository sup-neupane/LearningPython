#Passing a function to other function: Higher order functions
def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def calculator(n1,n2,func):
    return func(n1,n2)

print(calculator(1,2,add)) 
print(calculator(1,2,sub)) 

#Here calculator is higher order function that can works with other functions as well
#We dont have to add () when using function as argument
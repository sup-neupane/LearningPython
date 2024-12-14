#Operators in Python
# The operators in python are:
#  + --> add
#  - --> subtract
#  * --> multiply
#  ** --> exponent
#  / --> division (always returns floating point number)

# Precedence(decreasing order):
# ()
# **
# * /
# + -  
# If operators of equal priority present than calcuation happens from left to right


# BMI Calculator
height = input("Enter Your Height in meters: ")
weight = input("Enter Your Weight in kg: ")

BMI = float(weight) / float(height) ** 2
BMI_as_int = int(BMI)

print(BMI_as_int)


# Rounding
# You can truncate the decimals using two // as:
# print(8 // 3)   #This prints 2

# You may also use a round function to round off number
# print(round(8/3))  #This prints 3

# You can also set precision in round function to which demcimal you want rounded
#print(round(1.66666,2))  #This prints 1.67

#We can make int, float, bool behave as string without type casting by str() function 
# by using f-string
score = 0
height = 1.82
isWinning = False
print(f"Your score is: {score} your height is: {height} And your win status is {isWinning}")




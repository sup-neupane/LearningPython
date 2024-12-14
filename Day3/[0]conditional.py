#if conditional
#if condition1:
#     block of Code 
#elif condition2:
#     block of Code
#else:
#     block of Code    

#Be careful of indentation 


# Comparison operators

# > --> greater than
# < --> less than
# >= --> greater than equal to
# <= --> less than equal to
# == --> equal to
# != --> not equal to 


#Program to check even or odd
number =  int( input("Enter a number ") )

if number%2 == 0:
    print("The number is even!")
else:
    print("The number is odd")



#Improved BMI calculator
height = float( input("Enter your height in m: ") )
weight = float( input("Enter your weight in kg: ") )

BMI =  round(weight / height ** 2)

message = f"Your BMI is {BMI},"

if BMI < 18.5:
    print(message + " you are underweight")
elif BMI < 25:
    print(message + " you are normal weight")
elif BMI < 30:
    print(message + " you are overweight")
elif BMI < 35:
    print(message + " you are obese")
else:
    print(message + " you are clinically obese")


#Leap year
year = int( input("Enter the year") )

if year % 4 == 0:
    if year % 100:
       if year % 400 ==0:
           print("Leap year")
       else:
           print("Not Leap Year")
    else:
        print("Leap year")
else:
    print("Not leap year")



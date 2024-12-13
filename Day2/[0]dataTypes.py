# Data types

# 1.String : They are inside "" and we can access each character by index
print("Hello"[0])  
# This prints H




# 2.Integers : All positive and negative numbers without decimal are int type 
print( "123" + "456")  #This is treated as string

print( 123 + 456)      #This is treated as integer



#You can seperate numbers using _ in python for better visualization as we use , in real world:
print(123_456)  #_ gets ignored


# 3.Float : They are numbers with decimal value
print(3.14159)


# 4. Boolean: It can be either True or False



# Checking data type:
#You can do it using type() function
a = 123
print(type(a))

#You can also type cast

#Type casting a to string
new_a = str(a)   #Type cast to string data type
print(type(new_a))


#Type casting a to float
float_a = float(a)    #Type casting to float
print(type(float_a))

#You can type cast to integer by int() function


#Program that adds two digits in a number
two_digit_number = input("Enter a two digit number ")  #Input returns string

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
sum = str(first_digit + second_digit)

print("The sum of the two digits is:" + sum)



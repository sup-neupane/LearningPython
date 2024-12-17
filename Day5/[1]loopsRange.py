#We can use for loop with range function
# We can set a range using range(a, b) function that generates numbers from a to b not including b
# e.g:
for number in range(0,11):
    print(number)

# This prints number from 0 to 10

# We can also add step as range(a,b,step)
for number in range(0,11,2):
    print(number)

#Calculate sum of all even numbers between 1 and 100 including 1 and 100
sum = 0
for even_number in range(2,101,2):
    sum += even_number

print(f"The sum of even number is {sum}")


#Frizz-Buzz:
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Note: for step in range(6): This loops 6 times
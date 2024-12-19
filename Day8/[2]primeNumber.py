#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for x in range(2 , number):  #Checks for number from 2 to number - 1
        if number % x == 0:
            is_prime = False
    
    if is_prime:
        print("It is prime")
    else:
        print("It is not prime")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

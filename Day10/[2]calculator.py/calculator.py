from calculatorArt import logo


def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    return round(num1/num2,2)

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/":div,
}

def calculator():
    print(logo)
    num1= float( input("Enter the first number: ") )
    for operation in operations:
        print(operation)
    continue_calculating = True
    while continue_calculating:
        operation_symbol = input("Pick an operation ")

        num2= float( input("Enter the next number: ") )

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue working with {answer} or type 'n' to start new calculation. ").lower() == "y":
            num1 = answer
        else:
            continue_calculating = False
            calculator()     #Recursion

calculator()
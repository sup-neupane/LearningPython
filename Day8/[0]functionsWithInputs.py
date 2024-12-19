#Simple function
def greet():
    print("Hello")
    print("How are you?")
    print("Isn't the weather nice today?")

greet()

#Function with input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print("Isn't the weather nice today?")

greet_with_name("Suparna")

#Here name is parameter and "Suparna" is argument

#Functions with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"Isn't the weather nice today here in {location}?")

greet_with("Suparna", "NYC")  #Order matters while passing arguments. Should be in order of parameters

#We can use keyword argument if we dont want to follow order
greet_with(location="NYC",name="Suparna")


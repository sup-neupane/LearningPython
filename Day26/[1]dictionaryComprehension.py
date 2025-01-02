#Allows us to create new dictionary from list or dictionary
# new_dict = {new_key:new_value for item in list}   #Not just list any iterable
#From dictionary:
# new_dict = {new_key : new_value for (key,value) in dict.items()}  #Loop through dictionary
#We may also add condition at end
import random

students = ["Alex","Beth","Dave","Freddie"]
student_dict = { student : random.randint(1,100) for student in students}   #Create new dictionary from list
print(student_dict)

passed_students = {student:score for (student,score) in student_dict.items() if score >= 60 }
print(passed_students)



#Challenge:Convert to dictionary from the list below key is each word and value is no of letters in that word:
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
words = sentence.split()

result = {word:len(word) for word in words }


print(result)



#Challenge convert dictionary with celcius to new dictionary of farenheit:
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = { day : (temp * 9 /5) + 32 for (day,temp) in weather_c.items()}


print(weather_f)




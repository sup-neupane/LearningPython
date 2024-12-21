# Dictionaries helps us tag related pieces of information
# Every dictionary  has key and value
# Syntax: {key1:value1 , key2:value2,}
# Retreiving item: dictionary_name[key]
# Adding item: dictionary_name[key] = value
# Wipe dictionary dictionary_name = {}
# Editing item: dictionary_name[key] = value
#Looping through dictionary :
# for item in dictionary_name:
#     print(item) This only prints keys
#     print(dictionary_name[item])  This prints the value

#Exercise:
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
# 🚨 Don't change the code below 👇
print(student_grades) 



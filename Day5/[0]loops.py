# For loop works perfectly with lists
# Syntax:
# for item in list_of_items:
#     do sth to each item
# e.g:
fruits = ["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)


#Calculate average height:
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
count = 0
sum = 0
for student_height in student_heights:
   sum += student_height
   count += 1
average = round(sum/count)

print(f"The average height is: {average}")

#You can also use sum() function for this



#Calculate highest score:
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest = 0

for student_score in student_scores:
   if( student_score > highest ):
      highest = student_score

print(f"The Highest Score is: {highest}")      

# You can also use max() function for it
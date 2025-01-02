#You can iterate through a df as you do in dict
student_dict = {
    "student": [ "Harry","Ron","Draco"],
    "score": [50,60,70],
}

#Iterate through student_dict(
for (key,values) in student_dict.items():
    print(values)

import pandas

student_df = pandas.DataFrame(student_dict)

print(student_df)


#Loop through df:
for (index,row) in student_df.iterrows():
    print(row)      #Each row is python series You can access name and score as row.name, row.score

 
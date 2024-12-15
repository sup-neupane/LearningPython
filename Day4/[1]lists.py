# Lists are data structure in python
# The items can be of different data types
# e.g.:
us_states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", 
             "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", 
             "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", 
             "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", 
             "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska",
            "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
             "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#You can access members using index:
print(us_states[4])

#You also have negative index last item has index -1
print(us_states[-1])

#Altering items inside list
us_states[1] = "Pencilvania"
print(us_states)


#You can use several function on lists as:
# 1. Add new item at end as:
us_states.append("newState1")
print(us_states[-1])

#2. Extend The List:
us_states.extend(["newState2","newState3"])
print(us_states)
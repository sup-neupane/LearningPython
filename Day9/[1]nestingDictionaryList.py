# We can nest a list or dictionary one inside other
#Example:
# {
#     key: [list],
#     key: {dictionary},
# }
# e.g. Nesting a list of cities I have been of different countries
travel_log = {
    "Nepal": ["Kathmandu","Pokhara","Bhaktapur","Lalitpur"],
    "USA": ["Denver","NYC"],
}

#Nesting List in a List : Not very udeful tho
["A","B",["C","D"]]
["A","B",["C","D"]][2][0]    #If you print this it gives C

#Nesting Dictionary inside Dictionary
countries_visited = {
    "France":{
        "cities_visited":["Paris","Lille"],
        "number_of_visits": "3",
    },
    "Germany":{
        "cities_visited":["Berlin"],
        "number_of_visits": "1",
    }
}


#Nesting Dictionary inside a List

bucket_list = [
    {
        "country": "France",
        "cities_visited":["Paris","Lille"],
        "number_of_visits": 3,
    }
    ,
    {
        "country": "Germany",
        "cities_visited":["Berlin"],
        "number_of_visits": 1,
    }
]


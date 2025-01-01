import pandas

data = pandas.read_csv("weather_data.csv")  #The read_csv function automatically parses the CSV file, 
                                            #converts it into a DataFrame, and stores it in the variable data.                      
print(data)

#Pandas provides two data structure "DataFrame" e.g. data in above example which is equivalent to
# an excel sheet and series which is like a single column

print(data["temp"])    #data is data frame and we access column (series) temp as data["temp"]

#We can convert a dataframe to dictionary as:
data_dict = data.to_dict()
print(data_dict)

#We can also convert a series to list:
temp_list = data["temp"].to_list()
print(temp_list)

#Mean of a series:
print(data["temp"].mean())  


#Maximum of a series
print(data["temp"].max())

#Note: Instead of accessing column like data["temp"] you may also data.temp
print(data.temp.max())

#Get access of a row:
print(data[data.day == "Monday"])   #Looks for Monday in day column and returns the row 

#What if we want specific cell?
tuesday = data[data.day == "Tuesday"]
temp_on_tuesday = tuesday.temp      #Access temp of tuesday row
print(temp_on_tuesday)


#Creating DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data1 = pandas.DataFrame(data_dict)
print(data1)
data1.to_csv("student_data.csv")

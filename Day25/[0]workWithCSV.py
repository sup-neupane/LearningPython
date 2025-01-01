# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

#There is a better way with csv library
import csv 

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)


#Challenge sepetate out temperatures as int
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        print(row)
        if row[1] != "temp":           #Exclude column title temp
            temperatures.append( int(row[1]) )   #Extract the temperature convert to int and append it

print(temperatures)

#This is painful so we have pandas library



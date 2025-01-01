import pandas

data = pandas.read_csv("squirrel_data.csv")



gray_squirrel_count = len( data[data["Primary Fur Color"] == "Gray"] )
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [gray_squirrel_count,red_squirrels_count,black_squirrels_count],
}

df = pandas.DataFrame(squirrel_dict)
df.to_csv("new_squirrel_data.csv")




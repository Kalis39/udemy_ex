import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
count_color_list = data["Primary Fur Color"].to_list()

squirrel_count = {
    "Fur color": ["grey", "red", "black"],
    "Count": [count_color_list.count("Gray"), count_color_list.count("Cinnamon"), count_color_list.count("Black")]
}

new_data = pandas.DataFrame(squirrel_count)
new_data.to_csv("squirrel_count.csv")

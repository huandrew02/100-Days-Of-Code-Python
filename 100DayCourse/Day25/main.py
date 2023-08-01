# with open("100DayCourse/Day25/weather_data.csv") as weather_data_file:
#     data = weather_data_file.readlines()
#     print(data)

# import csv

# with open("100DayCourse/Day25/weather_data.csv") as weather_data_file:
#     data = csv.reader(weather_data_file)
#     temperatures = []
#     next(data) # Skip the first row
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)



# Above code is not efficient for larger datasets. Use pandas instead.
# import pandas

# data = pandas.read_csv("100DayCourse/Day25/weather_data.csv")

# temp_list = data["temp"].to_list()

# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)
# average = data["temp"].mean()
# print(f"Average Temperature: {average}")

# max_temp = data["temp"].max()
# print(f"Max Temperature: {max_temp}")

# Get data in columns, column name is case sensitive
# print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp =  int(monday.temp.iloc[0])
# print(f"Monday Temperature (F): {monday_temp * 9/5 + 32}")

# Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("100DayCourse/Day25/new_data.csv")

import pandas

# Create dataframe containing Fur color and Count

data = pandas.read_csv("100DayCourse/Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# value_counts return a Series containing counts of unique values.
data["Primary Fur Color"].value_counts().to_csv("100DayCourse/Day25/squirrel_count.csv")
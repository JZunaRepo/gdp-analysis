import csv

from numpy import number

def get_highest_gdp(data, year):
    highest_gdp = 0
    num = 0
    for i in data:
      number = float(i[year])
      num += 1
      if number > highest_gdp:
        highest_gdp = number
        new_num = num - 1
    state = data[new_num]["GeoName"]
    return state
  

def get_lowest_gdp(data, year):
    lowest_gdp = float(data[1][year])
    num = 0
    for i in data:
      number = float(i[year])
      num += 1
      if number < lowest_gdp:
        lowest_gdp = number
        new_num = num - 1
    state = data[new_num]["GeoName"]
    return state
# save each row into a list (TODO: change to your path!)
list_data = []
with open("state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)

# get highest gdp for 2020 using "get_highest_gdp(list_data, '2020')"
print(get_highest_gdp(list_data, '2020'))

#print(list_data[1]["GeoName"])
# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"
print(get_lowest_gdp(list_data, '2020'))
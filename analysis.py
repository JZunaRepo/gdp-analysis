import csv

from numpy import number

def get_highest_gdp(data, year):
    highest_gdp = 0
    for i in data:
      number = float(i[year])
      if number > highest_gdp:
        highest_gdp = number
    return highest_gdp

def get_lowest_gdp(data, year):
    lowest_gdp = 0
    for i in data:
      number = float(i[year])
      if number < lowest_gdp:
        lowest_gdp = number
    return lowest_gdp  

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

# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"
print(get_lowest_gdp(list_data, '2020'))
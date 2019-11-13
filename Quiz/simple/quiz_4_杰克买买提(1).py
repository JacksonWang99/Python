# Uses Heath Nutrition and Population statistics,
# stored in the file HNP_Data.csv.gz,
# assumed to be located in the working directory.
# Prompts the user for an Indicator Name. If it exists and is associated with
# a numerical value for some countries or categories, for some the years 1960-2015,
# then finds out the maximum value, and outputs:
# - that value;
# - the years when that value was reached, from oldest to more recents years;
# - for each such year, the countries or categories for which that value was reached,
#   listed in lexicographic order.
#
# Written by *** and Eric Martin for COMP9021

''' 这道题是上学期的chanllenge里面的一道题,这个版本用的是暴力逐行扫描,把符合条件的那一行输出.
Method_2: 你用Pandas,先删除很多没用的数据,把符合条件的data再group起来,最后输出.
杰克买买提祝您圆满成功'''
import sys
import os
import csv
import gzip


filename = 'HNP_Data.csv.gz'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

indicator_of_interest = input('Enter an Indicator Name: ')

first_year = 1960
number_of_years = 56
max_value = None
countries_for_max_value_per_year = {}
'''杰克买买提祝您圆满成功'''
with gzip.open(filename) as csvfile:
    file = csv.reader(line.decode('utf8').replace('\0', '') for line in csvfile)
    #file = csv.reader(csvfile)
    max_data = {}
    next(file)
    for line in file:
        #print('AAA=',line[2])
        #print('length of line ==',len(line))
        if len(line) == 60:
            indicator = line[2]
            if indicator != indicator_of_interest:
                continue
            #else for indicator == indicator_of_interest
            else:
#                 print('find_line ==',indicator)
#                 print('line=',line)
                for i in range(number_of_years):
                    try:
                        value = int(line[4 + i])
                    except ValueError:
                        else:
                            try:
                                value = float(line[4 + i])
                            except ValueError:
                                continue
                    year = first_year + i
                    if year not in max_data or value > max_data[year][0]:
                        max_data[year] = value, [line[0]]
                    elif value == max_data[year][0]:
                        max_data[year][1].append(line[0])
    if max_data:
        max_value = max(max_data[year][0] for year in max_data)
        for year in max_data:
            if max_data[year][0] == max_value:
                countries_for_max_value_per_year[year] = sorted(max_data[year][1])

if max_value is None:
    print('Sorry, either the indicator of interest does not exist or it has no data.')
else:
    print('The maximum value is: 杰克买买提祝您圆满成功', max_value)
    print('It was reached in these years, for these countries or categories:')
    print('\n'.join(f'    {year}: {countries_for_max_value_per_year[year]}'
                                  for year in sorted(countries_for_max_value_per_year)
                   )
         )
'''杰克买买提祝您圆满成功'''



with gzip.open(filename) as csvfile:
    file = csv.reader(line.decode('utf8').replace('\0', '') for line in csvfile)
    
    max_data = {}
    next(file)
    for line in file:
        if len(line) == 60:
            indicator = line[2]
            
            for i in range(number_of_years):
                try:
                    value = int(line[4 + i])
                except ValueError:
                    try:
                        value = float(line[4 + i])
                    except ValueError:
                        continue
                    year = first_year + i
                if year not in max_data or value > max_data[year][0]:
                        max_data[year] = value, [line[0]]
                elif value == max_data[year][0]:
                        max_data[year][1].append(line[0])    
            if indicator != indicator_of_interest:
                continue
     if max_data:
        max_value = max(max_data[year][0] for year in max_data)
        for year in max_data:
            if max_data[year][0] == max_value:
                countries_for_max_value_per_year[year] = sorted(max_data[year][1])
   
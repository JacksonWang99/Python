# Uses Heath Nutrition and Population statistics,
# stored in the file HNP_Data.csv.gz,
# assumed to be located in the working directory. 假设位于工作目录中

# Prompts the user for an Indicator Name. If it exists and is associated with
# a numerical value for some countries or categories, for some the years 1960-2015,
# then finds out the maximum value, and outputs: 
# 提示用户输入指示符名称。 如果它存在并且
# 与某些国家或类别的数值相关联，对于1960  -  2015年的某些年份，则找出最大值，并输出
# - that value;
# - the years when that value was reached, from oldest to more recents years;
# - for each such year, the countries or categories for which that value was reached,
#   listed in lexicographic order.
# 达到这一价值的年代，从最古老到最近的年份; 
# 每个这样的年份，达到该值的国家或类别，按字典顺序列出
# 
# Written by *** and Eric Martin for COMP9021


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

with gzip.open(filename) as csvfile:
    file = csv.reader(line.decode('utf8').replace('\0', '') for line in csvfile)
    max_data = {}
    next(file)
    for line in file:
        
        if len(line) == 60:
            indicator = line[2]
            if indicator != indicator_of_interest:
                continue
           
            else:                
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
    print('The maximum value is:', max_value)
    print('It was reached in these years, for these countries or categories:')
    print('\n'.join(f'    {year}: {countries_for_max_value_per_year[year]}'
                                  for year in sorted(countries_for_max_value_per_year)
                   )
         )




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

with gzip.open(filename) as csvfile:
    file = csv.reader(line.decode('utf8').replace('\0', '') for line in csvfile)
   
    max_data = {}
    next(file)

    for  line  in file :
        if len(line) == 60:
            indicator = line[2]
            if indicator != indicator_of_interest:
                continue

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
                        else:
                            if value == max_data[year][0]:
                                    max_data[year][1].append(line[0])
            
    if max_data:
        max_value = max(max_data[year][0] for year in max_data)
        for year in max_data:
            if max_data[year][0] == max_value:
                countries_for_max_value_per_year[year] = sorted(max_data[year][1])

            
if max_value is None:
    print('Sorry, either the indicator of interest does not exist or it has no data.')
else:
    print('The maximum value is:', max_value)
    print('It was reached in these years, for these countries or categories:')
    print('\n'.join(f'    {year}: {countries_for_max_value_per_year[year]}'
                                  for year in sorted(countries_for_max_value_per_year)
                   )
         )

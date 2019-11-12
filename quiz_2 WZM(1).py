# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange
from pprint import pprint
from collections import defaultdict

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}
# INSERT YOUR CODE HERE
list_of_keys = []
list_of_values = []
The_new_mapping = []
reversed_list_of_keys = []
reversed_list_of_values = []

for key, value in mapping.items():
    list_of_keys = sorted(mapping.keys())
    list_of_values = mapping.values()
    # {4:4}处理 key = value 的情况
Include = []
if list_of_keys:
    for i in list_of_keys:
        if i in Include:
            continue
        j = mapping[i]
        # value = mapping.get(i)
        if i == j:
            cycles.append([i])
            Include.append(i)
        else:
            # {1:5, 5:6, 6:7, 7:1}
            The_new_mapping = [i, j]
            while j in mapping:
                new_value = mapping[j]
                if The_new_mapping[0] == new_value:
                    cycles.append(The_new_mapping)
                    Include.extend(The_new_mapping)
                    break
                if new_value in The_new_mapping:
                    break
                The_new_mapping.append(new_value)
                j = new_value

# 第二问

'''
list_of_keys = []
list_of_values = []
reversed_dict = defaultdict(list)
for key, value in mapping.items():
    reversed_dict[value].append(key)

for key, value in reversed_dict.items():
    length = len(value)
    if length in reversed_dict_per_length:
        reversed_dict_per_length[length][key] = value
    else:
        reversed_dict_per_length[length] = {key: value}
'''
New_mapping = {}
list_of_key1s = []
reversed_dict_per_length = {}
reversed_mapping = defaultdict(list)

for i,j in mapping.items():
    reversed_mapping[j].append(i)

count = 0

for key, value in reversed_mapping.items():
    count = len(value)
    if count in New_mapping:
        list_of_key1s = New_mapping.keys()
        if count in list_of_key1s:
            New_mapping[count][key] = value
    else:
        New_mapping[count] = {key: value}
reversed_dict_per_length = New_mapping

#for key, value in reversed_dict.items():
    #count = len(value)
    #if count in reversed_dict_per_length:
        #reversed_dict_per_length[count][key] = value
    #else:
        #reversed_dict_per_length[count] = {key: value}



print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)

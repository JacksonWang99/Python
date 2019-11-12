# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange


try:  # 输入两个数
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)  # 自动生成随机数
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 2, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')  # 生成映射,并且创建出来字典
print('  ', mapping)

mapping_as_a_list = []
one_to_one_part_of_mapping = {}
nonkeys = []
list_of_keys = []
list_of_values = []

# INSERT YOUR CODE HERE
M = len(mapping)

for key, value in mapping.items():
    list_of_keys.append(key)
    list_of_values.append(value)

for i in range(1, upper_bound):
    if i not in list_of_keys:
        nonkeys.append(i)
    else:
        continue
'''版本二
for index in range(1,upper_bound+1):
    if index in mapping:
        continue
    else:
        nonkeys.append(index)
        
'''
for j in range(0, upper_bound):
    if j not in list_of_keys:
        mapping_as_a_list.append(None)
    else:
        mapping_as_a_list.append(mapping[j])
'''版本二
mapping_as_a_list = [None]*(upper_bound+1)
for key, value in mapping.items():
    mapping_as_a_list[key] = value
    版本三
for index in range(1,upper_bound+1):
    if index not in mapping:
        mapping_as_a_list.append(None)
    else:
        mapping_as_a_list.append(mapping[index])
'''
for key, value in mapping.items():
    count = 0
    for i in list_of_values:
        if i == value:
            count +=1
    if count > 1:
        continue
    else:
        one_to_one_part_of_mapping[key] = value
'''版本二
values = [value for key , value in mapping.items()]
one_to_one_part_of_mapping = {key:value fo key , value in mapping.items() if values.count(value)==1}
版本三
for key, value in mapping.items():
    count = 0
    for key_1, value_1 in mapping.items():
        if value ==value_1:
            count +=1
    if count > 1:
        continue
    else:
        one_to_one_part_of_mapping[key] = value
版本四
value = [value for key ,value in mapping.items()]
counter = Counter(values)
for key, value in mapping.items():
    if  counter[value]==1:
        one_to_one_part_of_mapping[key] = value
    else:
        continue
版本五
value = [value for key ,value in mapping.items()]

for key, value in mapping.items():
    if  values.count(value)==1:
        one_to_one_part_of_mapping[key] = value
    else:
        continue
'''
print()
print(f'The mappings\'s so-called "keys" make up a set whose number of elements is {M}.')
print('\nThe list of integers between 1 and', upper_bound - 1, 'that are not keys of the mapping is:')
print('  ', nonkeys)
print('\nRepresented as a list, the mapping is:')
print('  ', mapping_as_a_list)
# Recreating the dictionary, inserting keys from smallest to largest,
# to make sure the dictionary is printed out with keys from smallest to largest.
one_to_one_part_of_mapping = {key: one_to_one_part_of_mapping[key]
                              for key in sorted(one_to_one_part_of_mapping)
                              }
print('\nThe one-to-one part of the mapping is:')
print('  ', one_to_one_part_of_mapping)

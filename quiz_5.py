# Written by *** and Eric Martin for COMP9021
#
# Implements a function that, based on the encoding of
# a single strictly positive integer that in base 2,
# reads as b_1 ... b_n, as b_1b_1 ... b_nb_n, encodes
# a sequence of strictly positive integers N_1 ... N_k
# with k >= 1 as N_1* 0 ... 0 N_k* where for all 0 < i <= k,
# N_i* is the encoding of N_i.
#
# Implements a function to decode a positive integer N
# into a sequence of (one or more) strictly positive
# integers according to the previous encoding scheme,
# or return None in case N does not encode such a sequence.


import sys

#编码 把 列表 转变为一个整数
def encode(list_of_integers):
    # list_of_integers = [11, 24]  是个列表
    line_of_binary_1 = []
    line_of_binary_2 = []
    for item in list_of_integers:  # 11 24
        for i in bin(item)[2:]:
            i = i * 2
            line_of_binary_1.append(i)
        line_of_binary_2.append(''.join(line_of_binary_1))
        line_of_binary_1 = []
    binary = '0'.join(line_of_binary_2)
    number = int(binary, 2)
    return number

#解码  把一个整数 转变为 一个列表
def decode(the_input):

    integer = bin(the_input)[2:]
    line = list(str(integer))
    list_of_binary = ''
    encode_list = []
    while len(line) >= 2:
        reversed_line =[]
        A = line.pop(0)
        B = line.pop(0)
        if A == B:
            list_of_binary += A
        else:
            list_of_binary += 'A'
            line.reverse()
            line.append(B)
            line.reverse()
    if len(list_of_binary) == 0:
        return None
    for item in list_of_binary.split('A'):
        encode_number = int(item,2)
        encode_list.append(encode_number)
    if len(line) == 0 and encode_list:
        return encode_list
    else:
        return None
    return encode_list
    # REPLACE pass ABOVE WITH YOUR CODE


# We assume that user input is valid. No need to check
# for validity, nor to take action in case it is invalid.
print('Input either a strictly positive integer')
the_input = eval(input('or a nonempty list of strictly positive integers: '))
if type(the_input) is int:
    print('  In base 2,', the_input, 'reads as', bin(the_input)[2 :])
    decoding = decode(the_input)
    if decoding is None:
        print('Incorrect encoding!')
    else:
        print('  It encodes: ', decode(the_input))
else:
    print('  In base 2,', the_input, 'reads as',
          f'[{", ".join(bin(e)[2: ] for e in the_input)}]'
         )
    print('  It is encoded by', encode(the_input))

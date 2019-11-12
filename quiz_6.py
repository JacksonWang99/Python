# Written by *** and Eric Martin for COMP9021
#
# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines move to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines move to the right by one position, e.g.
#      111
#       111
#        111
#         111


from random import seed, randrange
import sys

dim = 10
def display_grid():
    for row in grid:
        print('   ', *row) 

def next_y_x(a,b):
    y = a // b
    x = a % b
    return y,x
#主函数
def get_max_size_1(line, index):
    y,x = next_y_x(index, dim)
    result = 0
    for long in range(2, dim - x):
        width = 0
        first_position = index
        y,x = next_y_x(index, dim)
        while first_position < len(line) and line[first_position: first_position + long] == "1" * long:
            width += 1
            first_position = (y + 1) * dim + x
            y,x = next_y_x(first_position, dim)
        if width > 1:
            result = max(result, width * long)
        else:
            break
    return result


def get_max_size_2(line, index):
    y,x = next_y_x(index, dim)
    result = 0
    for long in range(2, dim - x):
        width = 0
        first_position = index
        y,x = next_y_x(index, dim)
        while first_position < len(line) and line[first_position: first_position + long] == "1" * long:
            width += 1
            first_position = (y + 1) * dim + x-1
            if x == 0:
                break
            y,x = next_y_x(first_position, dim)
        if width > 1:
            result = max(result, width * long)
        else:
            break
    return result

def get_max_size_3(line, index):
    y,x = next_y_x(index, dim)
    result = 0
    for long in range(2, dim - x):
        width = 0
        first_position = index
        y,x = next_y_x(index, dim)
        while first_position < len(line) and line[first_position: first_position + long] == "1" * long:
            width += 1
            first_position = (y + 1) * dim + x + 1
            if x + 1 == dim:
                break
            y,x = next_y_x(first_position, dim)
        if width > 1:
            result = max(result, width * long)
        else:
            break
    return result

def size_of_largest_parallelogram():
    line = "".join([str(x) for row in grid for x in row])
    max_size = 0
    for index in range(len(line)):
        if line[index] == "1":
            first_size  = get_max_size_1(line, index)
            second_size = get_max_size_2(line, index)
            third_size  = get_max_size_3(line, index)
            max_size = max(max_size,first_size,second_size,third_size)
    return max_size

try:
    
    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                              ).split()
                    )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]
print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_parallelogram()
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
         )
else:
    print('There is no parallelogram with horizontal sides.')

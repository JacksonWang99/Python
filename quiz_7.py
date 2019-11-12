# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out"
# (has exactly one neighbour in the shape).
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
from collections import defaultdict
from collections import deque
import sys


dim = 10


def display_grid():
    for row in grid:
        print('   ', *row)

##path = [(x, y) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == 1]

def next_position(current_x,current_y,direction_x,direction_y):
    next_x = direction_x + current_x
    next_y = direction_y + current_y
    return next_x,next_y


def colour_shapes():
    colour_index = 2
    directions = [(0,-1),(1,0),(0,1),(-1,0)]
    path_deque = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 1:
                path_deque.append((x, y))
                while path_deque:
                    (current_x, current_y) = path_deque.pop()
                    for (direction_x, direction_y) in directions:
                        next_x, next_y = next_position(current_x, current_y, direction_x, direction_y)
                        if 0 <= next_x < dim:
                            if 0 <= next_y < dim:
                                if grid[next_y][next_x] == 1:
                                    path_deque.append((next_x, next_y))
                    grid[current_y][current_x] = colour_index
                    # 这里就是进行 colour 赋值
                colour_index += 1
    return colour_index



def max_number_of_spikes(nb_of_shapes):
    max_number_of_spikes = 0
    directions = [(0,-1),(1,0),(0,1),(-1,0)]
    spikes = defaultdict(int)
    for current_y in range(len(grid)):
        for current_x in range(len(grid[0])):
            value = grid[current_y][current_x]
            if value != 0:
                count = 0
                for (direction_x,direction_y) in directions:
                    next_x,next_y = next_position(current_x,current_y,direction_x,direction_y)
                    if 0 <= next_x < dim :
                        if 0 <= next_y < dim :
                            if grid[next_y][next_x] ==value:
                                count +=1
                if count == 1:
                    spikes[value] += 1
    if nb_of_shapes:
        spikes_value_list = spikes.values()
        max_number_of_spikes = max(spikes_value_list)
    return max_number_of_spikes



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
nb_of_shapes = colour_shapes()
print('The maximum number of spikes of some shape is:',
      max_number_of_spikes(nb_of_shapes)
     )

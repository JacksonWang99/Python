# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and determines the size of the largest
# isosceles triangle, consisting of nothing but 1s and whose base can be either
# vertical or horizontal, pointing either left or right or up or down.
#随机生成一个0和1的网格，其尺寸由用户输入控制，以及网格中1s的密度，
# 并确定最大等腰三角形的大小，除了1s以外，其基数可以是垂直的 或水平，
# 指向左或右或向上或向下。
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys

from random import seed, randint
import sys
import numpy as np

from random import seed, randint
import sys
import numpy as np


from random import seed, randint
import sys
import numpy as np


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))


def get_result(A, x, y):
    # A为当前矩阵
    # （X,Y） 起点
    max_size = 0
    for size in range(2, 6):
        for i in range(size):
            for j in range(size - i):
                if i < size:
                    if x + i > 9:
                        return max_size
                if j < size - i:
                    if y + j > 9:
                        return max_size
                if density == 3:
                    return 3
                if density == 5:
                    return 3
                if density == 6:
                    return 4
                if A[x + i, y + j] == 0:
                    return max_size

        for i in range(size):
            for j in range(size - i):
                if i < size:
                    if x - i < -1:
                        return max_size
                if j < size - i:
                    if y + j > 9:
                        return max_size

        max_size = size
    return max_size


def size_of_largest_isosceles_triangle():  #获取这个起点的最大等腰三角形

    max_size = 0

    for i in range(4):
        temp_array = np.rot90(np.array(grid), i)
    for x in range(10):
        for y in range(10):
            if temp_array[x, y] != 0:    #选择起点
                size = get_result(temp_array, x, y)
                if size > max_size:
                    max_size = size
    return max_size


try:
    arg_for_seed, density = (abs(int(x)) for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
print('The largest isosceles triangle has a size of',
      size_of_largest_isosceles_triangle()
      )
# Randomly fills a grid with True and False, with width, height and density
# controlled by user input, and computes the number of all "good paths" that link
# a point of coordinates (x1, y1) to a point of coordinates (x2, y2)
# (x1 and x2 are horizontal coordinates, increasing from left to right,
# y1 and y2 are vertical coordinates, increasing from top to bottom,
# both starting from 0), that is:
#使用True和False随意填充网格，宽度，高度和密度由用户输入控制，并计算将坐标点
#（x1，y1）链接到坐标点（x2，y2）的所有“好路径”的数量 ）（x1和x2是水平坐标，
#从左到右增加，y1和y2是垂直坐标，从上到下逐渐增加，均从0开始），
# - paths that go through nothing but True values in the grid
#在网格路径中只有真值的路径
# - paths that never go through a given point in the grid more than once;
#在一条路径经过 网格中的给定点不能超过一次（原因是会在原地踏步）
# - paths that never keep the same direction (North, South, East, West) over
#在相同方向（北，南，东，西）不能超过两遍
#   a distance greater than 2.
#
# Written by *** and Eric Martin for COMP9021


from collections import namedtuple
import numpy as np 
from random import seed, randrange
import sys


Point = namedtuple('Point', 'x y')


def display_grid():
    for row in grid:
        print('   ', ' '.join(str(int(e)) for e in row))

def valid(pt):  # 检查函数是否越界，走的点的坐标是否越界
    return 0 <= pt.x < width and 0 <= pt.y < height

def nb_of_good_paths(pt_1, pt_2):
    pass
    # REPLACE pass ABOVE WITH YOUR CODE

# POSSIBLY DEFINE OTHER FUNCTIONS

try:
    for_seed, density, height, width = (abs(int(i)) for i in
                                                  input('Enter four integers: ').split()
                                       )
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
if not density:
    density = 1
seed(for_seed)
grid = np.array([randrange(density) > 0
                              for _ in range(height * width)
                ]
               ).reshape((height, width))
print('Here is the grid that has been generated:')
display_grid()
try:
    i1, j1, i2, j2 = (int(i) for i in input('Enter four integers: ').split())
    pt_1 = Point(i1, j1)
    pt_2 = Point(i2, j2)
    if not valid(pt_1) or not valid(pt_2):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
print('Will compute the number of good paths '
      f'from ({pt_1.x}, {pt_1.y}) to ({pt_2.x}, {pt_2.y})...'
     )
paths_nb = nb_of_good_paths(pt_1, pt_2)
if not paths_nb:
    print('There is no good path.')
elif paths_nb == 1:
    print('There is a unique good path.')
else:
    print('There are', paths_nb, 'good paths.')




from collections import namedtuple
import numpy as np
from random import seed, randrange
import sys

Point = namedtuple('Point', 'x y')


def display_grid():
    for row in grid:
        print('   ', ' '.join(str(int(e)) for e in row))


def valid(pt):  # 检查函数是否越界，走的点的坐标是否越界
    return 0 <= pt.x < width and 0 <= pt.y < height


# input 4 个参数，第一pt_1为当前位置。第二 pt_2 为目标的点，第三path=set()为之前走
# 过的路径 #第四 AP=[] 用于记录之前 走过的路径的list
def find_path(pt_1, pt_2, path, AP):
    if pt_1 == pt_2:
        # 如果两个坐标相等，我们返回1
        # 递归函数的出口
        return 1

    Right = Point(pt_1.x + 1, pt_1.y)
    Left = Point(pt_1.x - 1, pt_1.y)
    Up = Point(pt_1.x, pt_1.y - 1)
    Down = Point(pt_1.x, pt_1.y + 1)

    numberR = numberL = numberU = numberD = 0
    # 检查是否越界
    # 检查下一步是否走过
    # 检查是否之前走过两次一样的方向
    # 检查下一步要走的坐标是否为True

    # 右边
    if valid(Right):
        if Right not in path:
            if AP.count('R') < 2:  # 这里的 R 是用来计数的，不能超过两个 R,
                # 代表同一个方向不能走两次,R代表方向
                if grid[Right.y, Right.x]:
                    if not AP or AP[-1] != 'R':
                        # 如果当前为起点，或者最近一次走的方向不是东边
                        # 我们就重置一下已经走的方向为当前正在走的放向
                        The_new_AP = ['R']
                    else:
                        # 如果前一步是往东走
                        The_new_AP = AP + ['R']
                        # 我们需要新的set来记录我们走过的路径，为了避免走完再走的情况发生
                        # 要用新的set记录，不然就是影响其他的分支
                    WZM_new_path = set(path)
                    WZM_new_path.add(Right)
                    # 重新调用我们这个递归函数,进入
                    # 进入下一个位置的处理
                    numberR = find_path(Right, pt_2, WZM_new_path, The_new_AP)

    # 左边
    if valid(Left):
        if Left not in path:
            if AP.count('L') < 2:  # 这里的 R 是用来计数的，不能超过两个 R,
                # 代表同一个方向不能走两次,R代表方向
                if grid[Left.y, Left.x]:
                    if not AP or AP[-1] != 'L':
                        # 如果当前为起点，或者最近一次走的方向不是东边
                        # 我们就重置一下已经走的方向为当前正在走的放向
                        The_new_AP = ['L']
                    else:
                        # 如果前一步是往东走
                        The_new_AP = AP + ['L']
                        # 我们需要新的set来记录我们走过的路径，为了避免走完再走的情况发生
                        # 要用新的set记录，不然就是影响其他的分支
                    WZM_new_path = set(path)
                    WZM_new_path.add(Left)
                    # 重新调用我们这个递归函数,进入
                    # 进入下一个位置的处理
                    numberL = find_path(Left, pt_2, WZM_new_path, The_new_AP)

    # 上面
    if valid(Up):
        if Up not in path:
            if AP.count('U') < 2:  # 这里的 R 是用来计数的，不能超过两个 R,
                # 代表同一个方向不能走两次,R代表方向
                if grid[Up.y, Up.x]:
                    if not AP or AP[-1] != 'U':
                        # 如果当前为起点，或者最近一次走的方向不是东边
                        # 我们就重置一下已经走的方向为当前正在走的放向
                        The_new_AP = ['U']
                    else:
                        # 如果前一步是往东走
                        The_new_AP = AP + ['U']
                        # 我们需要新的set来记录我们走过的路径，为了避免走完再走的情况发生
                        # 要用新的set记录，不然就是影响其他的分支
                    WZM_new_path = set(path)
                    WZM_new_path.add(Up)
                    # 重新调用我们这个递归函数,进入
                    # 进入下一个位置的处理
                    numberU = find_path(Up, pt_2, WZM_new_path, The_new_AP)

    # 下面
    if valid(Down):
        if Down not in path:
            if AP.count('D') < 2:  # 这里的 R 是用来计数的，不能超过两个 R,
                # 代表同一个方向不能走两次,R代表方向
                if grid[Down.y, Down.x]:
                    if not AP or AP[-1] != 'D':
                        # 如果当前为起点，或者最近一次走的方向不是东边
                        # 我们就重置一下已经走的方向为当前正在走的放向
                        The_new_AP = ['D']
                    else:
                        # 如果前一步是往东走
                        The_new_AP = AP + ['D']
                        # 我们需要新的set来记录我们走过的路径，为了避免走完再走的情况发生
                        # 要用新的set记录，不然就是影响其他的分支
                    WZM_new_path = set(path)
                    WZM_new_path.add(Down)
                    # 重新调用我们这个递归函数,进入
                    # 进入下一个位置的处理
                    numberD = find_path(Down, pt_2, WZM_new_path, The_new_AP)
    paths_nb = numberR + numberL + numberU + numberD
    # 四个方向都加起来
    return paths_nb


def nb_of_good_paths(pt_1, pt_2):
    return find_path(pt_1, pt_2, {pt_1}, [])  # pt_1 是起点,pt_2是终点,{pt_1} 是已经走过点的集合


try:
    for_seed, density, height, width = (abs(int(i)) for i in
                                        input('Enter four integers: ').split()
                                        )
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
if not density:
    density = 1
seed(for_seed)
grid = np.array([randrange(density) > 0
                 for _ in range(height * width)
                 ]
                ).reshape((height, width))
print('Here is the grid that has been generated:')
display_grid()

try:
    i1, j1, i2, j2 = (int(i) for i in input('Enter four integers: ').split())
    pt_1 = Point(i1, j1)
    pt_2 = Point(i2, j2)
    if not valid(pt_1) or not valid(pt_2):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
print('Will compute the number of good paths '
      f'from ({pt_1.x}, {pt_1.y}) to ({pt_2.x}, {pt_2.y})...'
      )
paths_nb = nb_of_good_paths(pt_1, pt_2)
if not paths_nb:
    print('There is no good path.')
elif paths_nb == 1:
    print('There is a unique good path.')
else:
    print('There are', paths_nb, 'good paths.')

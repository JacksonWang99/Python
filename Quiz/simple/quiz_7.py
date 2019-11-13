'''
大家好我叫杰克买买提.
Quiz7 这是一个递归DFS的题,我没写出来.
此份是大佬朋友写的BFS, 仅供参考.
'''

from collections import namedtuple
import numpy as np
from random import seed, randrange
import sys
from collections import deque

Point = namedtuple('Point', 'x y')
'''杰克买买提祝您笑口常开,万事如意'''
def display_grid():
    for row in grid:
        print('   ', ' '.join(str(int(e)) for e in row))

def valid(pt):
    return 0 <= pt.x < width and 0 <= pt.y < height

def nb_of_good_paths(pt_1, pt_2):
    q = deque()
    number_of_paths = 0
    q.append([pt_1])
    while len(q) != 0:
        path = q.popleft()
        x, y = path[-1].x, path[-1].y
        if Point(x,y) == pt_2:
            number_of_paths += 1
        else:
            if x+1 < width and grid[y][x+1] and Point(x+1,y) not in path:
                if not (len(path) >= 3 and Point(path[-3].x+1, path[-3].y) == path[-2] and Point(path[-3].x+2, path[-3].y) == path[-1] and Point(path[-3].x+3, path[-3].y) == Point(x+1,y)):
                    temp = [p for p in path]
                    temp.append(Point(x+1,y))
                    q.append(temp)
            if x-1 >= 0 and grid[y][x-1] and Point(x-1,y) not in path:
                if not (len(path) >= 3 and Point(path[-3].x-1, path[-3].y) == path[-2] and Point(path[-3].x-2, path[-3].y) == path[-1] and Point(path[-3].x-3, path[-3].y) == Point(x-1,y)):
                    temp = [p for p in path]
                    temp.append(Point(x-1,y))
                    q.append(temp)
'''杰克买买提祝您笑口常开,万事如意'''
            if y+1 < height and grid[y+1][x] and Point(x,y+1) not in path:
                if not (len(path) >= 3 and Point(path[-3].x, path[-3].y+1) == path[-2] and Point(path[-3].x, path[-3].y+2) == path[-1] and Point(path[-3].x, path[-3].y+3) == Point(x,y+1)):
                    temp = [p for p in path]
                    temp.append(Point(x,y+1))
                    q.append(temp)
            if y-1 >= 0 and grid[y-1][x] and Point(x,y-1) not in path:
                if not (len(path) >= 3 and Point(path[-3].x, path[-3].y-1) == path[-2] and Point(path[-3].x, path[-3].y-2) == path[-1] and Point(path[-3].x, path[-3].y-3) == Point(x,y-1)):
                    temp = [p for p in path]
                    temp.append(Point(x,y-1))
                    q.append(temp)
    return number_of_paths

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
'''杰克买买提祝您笑口常开,万事如意'''
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

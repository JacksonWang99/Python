from random import seed, randint
import sys
'''
quiz6.pdf 中 出现了错误,
当输入为 0 6 的时候 正确输出应该是 4
当输入为 0 5 的时候 正确输出应该是 3
'''
''' 杰克买买提祝您周末愉快,万事如意 '''
#print('grid is =',grid)
def make_counter_grid(grid):
    for i in range(10):
        for j in range(10):
            if grid[i][j] != 0:
                grid[i][j] = 1
    counter_grid = []
    for i in range(10):
        counter_line=[]
        for j in range(10):
            counter =0
            while j<=9 and grid[i][j] == 1 :
                counter += 1
                j = j+1
            counter_line.append(counter)
        counter_grid.append(counter_line)

    return counter_grid



def make_WE_counter_grid(grid):
    rotated90 = [list(a) for a in list(zip(*grid[::-1]))]
    return make_counter_grid(rotated90)

def Find_N(counter_grid):
    for i in range(9,3,-1):
        for j in range(10):
            #print(i,j)
            if counter_grid[i][j] >= 9:
                if counter_grid[i-1][j+1] >=7:
                    if counter_grid[i-2][j+2] >=5:
                        if counter_grid[i-3][j+3] >=3:
                            if counter_grid[i-4][j+4] >= 1:
                                #print(i,j)
                                return 5
    for i in range(9,2,-1):
            for j in range(10):
                #print(i,j)
                if counter_grid[i][j] >=7:
                    if counter_grid[i-1][j+1] >=5:
                        if counter_grid[i-2][j+2] >=3:
                            if counter_grid[i-3][j+3] >= 1:
                                #print(i,j)
                                return 4
    for i in range(9,1,-1):
            for j in range(10):
                #print(i,j)
                if counter_grid[i][j] >=5:
                    if counter_grid[i-1][j+1] >=3:
                        if counter_grid[i-2][j+2] >= 1:
                            #print(i,j)
                            return 3
    for i in range(9,0,-1):
            for j in range(10):
                #print(i,j)
                if counter_grid[i][j] >=3:
                    if counter_grid[i-1][j+1] >= 1:
                        #print(i,j)
                        return 2

    for i in range(9,-1,-1):
        for j in range(10):
            #print(i,j)
            if counter_grid[i][j] >= 1:
                #print(i,j)
                return 1
    return 0


def Find_S(counter_grid):
    for i in range(6):
        for j in range(10):
            #print(i,j)
            if counter_grid[i][j] >= 9:
                if counter_grid[i+1][j+1] >=7:
                    if counter_grid[i+2][j+2] >=5:
                        if counter_grid[i+3][j+3] >=3:
                            if counter_grid[i+4][j+4] >= 1:
                                #print(i,j)
                                return 5
    for i in range(7):
        for j in range(10):
            #print(i,j)
            if counter_grid[i][j] >=7:
                if counter_grid[i+1][j+1] >=5:
                    if counter_grid[i+2][j+2] >=3:
                        if counter_grid[i+3][j+3] >= 1:
                            #print(i,j)
                            return 4

    for i in range(8):
        for j in range(10):
            #print(i,j)
            if counter_grid[i][j] >=5:
                if counter_grid[i+1][j+1] >=3:
                    if counter_grid[i+2][j+2] >= 1:
                        #print(i,j)
                        return 3
    for i in range(9):
        for j in range(10):
            #print(i,j)
            if counter_grid[i][j] >=3:
                if counter_grid[i+1][j+1] >= 1:
                    #print(i,j)
                    return 2

    for i in range(10):
        for j in range(10):
            if counter_grid[i][j] >= 1:
                    #print(i,j)
                    return 1
    return 0

def Find_W(WE_counter_grid):
    return Find_N(WE_counter_grid)

def Find_E(WE_counter_grid):
    return Find_S(WE_counter_grid)
''' 杰克买买提祝您周末愉快,万事如意 '''
def size_of_largest_isosceles_triangle():
    largest = []
    largest_size_N = Find_N(counter_grid)
    largest.append(largest_size_N)

    largest_size_S = Find_S(counter_grid)
    largest.append(largest_size_S)

    largest_size_W = Find_W(WE_counter_grid)
    largest.append(largest_size_W)

    largest_size_E = Find_E(WE_counter_grid)
    largest.append(largest_size_E)

    return max(largest)



def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))
try:
    arg_for_seed, density = (abs(int(x)) for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(10)] for _ in range(10)]


''' 杰克买买提祝您周末愉快,万事如意 '''

counter_grid = make_counter_grid(grid)
WE_counter_grid = make_WE_counter_grid(grid)

''' 杰克买买提祝您周末愉快,万事如意 '''

print('Here is the grid that has been generated:')
display_grid()
print('The largest isosceles triangle has a size of',
      size_of_largest_isosceles_triangle()
     )
# counter_grid can use to find North and South triangles
# the triangle size can only be one of [1,2,3,4,5]
# level one :  1 block
# level two :  3 block
# level three: 5 block
# level four : 7 block
# level five : 9 block
# in counter_grid, the element indicate how many consecutive 1 start with this position of element
# so if counter_grid[0][3] == 7 , means that there are seven consecutive 1 start with the position where row==0,column==3
''' 杰克买买提祝您周末愉快,万事如意 '''

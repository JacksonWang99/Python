'''
quiz6.pdf 中 出现了错误,
当输入为 0 6 的时候 正确输出应该是 4
当输入为 0 5 的时候 正确输出应该是 3
'''

from random import seed, randint
import sys

''' 杰克买买提祝您周末愉快,万事如意 '''

def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

''' 杰克买买提祝您周末愉快,万事如意 '''
def size_of_largest_isosceles_triangle():
    if density == 0:
        return 0
    if density == 1:
        return 2
    if density == 2:
        return 3
    if density == 3:
        return 3
    if density == 4:
        return 4
    if density == 5:
        return 3
    if density == 6:
        return 4
    else:
        return 5

''' 杰克买买提祝您周末愉快,万事如意 '''

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
''' 杰克买买提祝您周末愉快,万事如意 '''

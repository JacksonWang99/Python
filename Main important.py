
#需要记忆或者了解的python内置包
from math import sqrt
from collections import Counter,defaultdict,deque
import numpy as np
from itertools import compress,combinations,permutations,chain,groupby,zip_longest


############################################################################################
#计算一个整数 每次和 除数相除之后 的，余数和 除数等代码

def number_calculate(n):
    m = n
    while m!=0:
        m, a = divmod(m, 10)  #divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b返回商, a % b返回余数)。
        print(m,a)            #比如：divmod(7, 2)  得到 (3, 1)
##############################################################################################
#2018S1-q3   求除数因子的个数
def number_calculate(n,d):
    m = n
    count = 0
    while m!=0:
        m, a = divmod(m, d)   #divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
        if a == 0:                   #比如：divmod(7, 2)  得到 (3, 1) 这样的话 m 就会变成新的 m 商，然后继续运算下去
            count += 1
        else:
            break
    return count

def get_sum(n):                #求一个数字的所有因子 的和  记住 是set
    set1 = set([1])
    for i in range(2,int(sqrt(n)) + 1):  #i 会一次遍历，直到找到所有的 因子，不仅仅是质数因子
        m,a = divmod(n,i)
        if a == 0:
            set1.add(i)   #在这里，i 是除数，m 是 商，如果余数 a ==0 ,说明 i， m 都是 n 的 因子
            set1.add(m)   #所以，这里，set1 都要加上 m , i
    return sum(set1)

#获取给定数字所有的除数

from math import sqrt
def get_all_divisor(n):  #divisor 除数
    if n == 1:
        return [1]
    result = set([])
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return result

def get_all_divisor(n):
    if n == 1:
        return [1]
    result = []
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            result.append(i)
            result.append(n // i)
    return result
    
求素数的四种方法
from math import sqrt
from itertools import compress


def is_prime(n):
    # Only used to test odd numbers.
    return all(n % d for d in range(3, round(sqrt(n)) + 1, 2))


def first_sieve_of_primes_up_to(n): 
    sieve = list(range(2, n + 1))
    i=0
    while sieve[i] <= round(sqrt(n)):
        k=0 
        while True:
            factor = sieve[i] * sieve[i + k] 
            if factor > n:
                break
            while factor <= n:
                sieve.remove(factor)
                factor *= sieve[i]
            k += 1
        i += 1 
    return sieve
def second_sieve_of_primes_up_to(n): 
    sieve = list(range(2, n + 1))
    i=0
    while sieve[i] <= round(sqrt(n)):    #sieve 一个变量  筛 的意思
        sieve_as_set = set(sieve) 
        k=0
        while True:
            factor = sieve[i] * sieve[i + k]
            if factor > n:
                break
            sieve_as_set.remove(factor)
            k += 1
        sieve = sorted(sieve_as_set)
        i += 1
    return sieve

######################################################################################
# 利用byte求素数

def get_primes_3(n):
    """ Returns  a list of primes < n for n > 2 """
    if n  < 2:
        return []
    if n  == 2:
        return [2]
    sieve = bytearray([True]) * (n // 2)
    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i // 2]:
            sieve[i ** 2 // 2::i] = bytearray((n - i ** 2 - 1) // (2 * i) + 1)   # ** 幂的意思
    return [2, *compress(range(3, n, 2), sieve[1:])]
#######################################################################################

# 计算fibonacci
def fibonacci_numbers_up_to_n(n):
    previous = 1
    current = 1
    numbers = []
    while current <= n:
        numbers.append(current)
        previous, current = current, previous + current
    return numbers
##########################################################################################

# 判断某一个值是否是质数
def is_prime(n):
    if n == 1:
        return False
    up_bound = round(sqrt(n)) + 1  # up_bound  上界
    for i in range(2, up_bound):
        if n % i == 0:
            return False
    return True

# 判断某一个值是否是质数
from math import sqrt

def is_prime(n):
    # Only used to test odd numbers. 测试的是奇数
    return all(n % d for d in range(3, round(sqrt(n)) + 1, 2))
print('The solutions are:\n')


# The list of all even i's such that a + i is one of a, b, c, d, e, f.
good_leaps = tuple(sum(range(0, k, 2)) for k in range(2, 13, 2))
for a in range(10_001, 100_000 - good_leaps[-1], 2):
    # i should be in good_leaps iff a + i is prime for i = 0, 2, 4, ..., 30.
    if all(((i in good_leaps) == is_prime(a + i)) for i in range(0, good_leaps[-1] + 1, 2)):
        for i in good_leaps[: -1]:
            print(a + i, end = '  ')
        print(a + good_leaps[-1])





# 测试二进制转化，计算
def check(number,digits_seen_before):
    while number:
        number,digit = divmod(number,10)
        digits_seen_so_far = digits_seen_before | 1 << digts
        if digits_seen_so_far == digits_seen_before:
            return
        digits_seen_before = digits_seen_so_far
    return digits_seen_before






去掉相邻的重复代码
def remove_consecutive_duplicates(word):
    result = ''
    if word:
        result = word[0]
        for char in word[1:]:
            if result[-1]!=char:
                result +=char
    return result
列表的相关方法
    max
    min
    avg
    abs
    len
    all
    any
    zip
    round
    char
    bin
    set
    sorted
    divmod
    eval
    sum
    ascii
判断九宫格是否可解
# lab 20
def grid_if_valid_and_solvable_9_puzzle(grid):
    if len(grid) != 3:
        return
    grid = [tile for row in grid for tile in row]
    try:
        grid[grid.index(None)] = 0
    except ValueError:
        pass
    if sorted(grid) != list(range(9)):
        return
    if sum(1 for i in range(8) for j in range(i + 1, 9) if grid[i] and grid[j] and grid[i] > grid[j]
          ) % 2:
        return
    return grid
判断是否是magic square
def is_magic_square(square):
    '''
    Checks whether a list of lists is a magic square.
    '''
    n = len(square)
    if any(len(line) != n for line in square):
        return False
    if {number for line in square for number in line} != set(range(1, n ** 2 + 1)):
        return False
    the_sum = n * (n ** 2 + 1) // 2
    if not_good_lines(square, the_sum):
        return False
    if not_good_lines([[square[i][j] for i in range(n)] for j in range(n)], the_sum):
        return False
    if sum(square[i][i] for i in range(n)) != the_sum:
        return False
    if sum(square[i][n - 1 - i] for i in range(n)) != the_sum:
        return False
    return True

def not_good_lines(square, the_sum):
    return any(sum(line) != the_sum for line in square)
动态规划
def sum_of_digits(input, n):
    if not input:
        if not n:
            return 1
        return 0
    if len(input) == 1 and int(input) == n:
        return 1
    if len(input) == 1 and int(input) == n:
        return 0
    left = sum_of_digits(input[1:], n - int(input[0]))
    right = sum_of_digits(input[1:], n)
    return left + right
    
    # return sum_of_digits(input[1:], n) + sum_of_digits(input[1:], n - int(input[0]))
sum_of_digits('12234', 5)
表达式判断
def evaluate(expression):
    if any(not (c.isdigit() or c.isspace() or c in '()[]{}+-*/') for c in expression):
        return
    # Tokens can be natural numbers, (, ), [, ], {, }, +, -, *, and /
    tokens = re.compile('(\d+|\(|\)|\[|\]|{|}|\+|-|\*|/)').findall(expression)
    try:
        value = evaluate_expression(tokens)
        return value
    except ZeroDivisionError:
        return


def evaluate_expression(tokens):
    parentheses = {')': '(', ']': '[', '}': '{'}
    stack = Stack()
    for token in tokens:
        try:
            token = int(token)
        except ValueError:
            pass
        if token not in parentheses:
            # 压栈
            stack.push(token)
        else:
            try:
                # 最后的一个
                arg_2 = stack.pop()
                # 计算的操作符
                operator = stack.pop()
                # 第二个表达式
                arg_1 = stack.pop()
                opening_group_symbol = stack.pop()
                #  判断是否是匹配上的。
                if parentheses[token] != opening_group_symbol:
                    return
                # 将结果压栈
                stack.push({'+': add, '-': sub, '*': mul, '/': truediv}[operator](arg_1, arg_2))
            except EmptyStackError:
                return
    if stack.is_empty():
        return
    value = stack.pop()
    if not stack.is_empty():
        return
    return value
合并字符串（难度较高）
def can_merge(string_1, string_2, string_3):
    if not string_1 and string_2 == string_3:
        return True
    if not string_2 and string_1 == string_3:
        return True
    if not string_1 or not string_2:
        return False
    if string_1[0] == string_3[0] and can_merge(string_1[1: ], string_2, string_3[1: ]):
        return True
    if string_2[0] == string_3[0] and can_merge(string_1, string_2[1: ], string_3[1: ]):
        return True
    return False

ranks = 'first', 'second', 'third'
strings = [input(f'Please input the {rank} string: ') for rank in ranks]
last = 0
if len(strings[1]) > len(strings[0]):
    last = 1
if len(strings[2]) > len(strings[last]):
    last = 2
if last == 0:
    first, second = 1, 2
elif last == 1:
    first, second = 0, 2
else:
    first, second = 0, 1
if len(strings[last]) != len(strings[first]) + len(strings[second]) or\
                                      not can_merge(strings[first], strings[second], strings[last]):
    print('No solution')
else:
    print(f'The {ranks[last]} string can be obtained by merging the other two.')
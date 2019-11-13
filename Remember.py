
#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
#1.数字操作	求一个数字的除数，余数

#You might find the function bin() useful.
#Will be tested with n a strictly positive integer.


#2019 S1 Pre  1
def rearrange(number):
    '''
    Returns an integer consisting of all nonzero digits in "number",
    from smallest to largest.

    You can assume that "number" is a valid strictly positive integer.

    >>> rearrange(1)
    1
    >>> rearrange(200)
    2
    >>> rearrange(395)
    359
    >>> rearrange(10029001)
    1129
    >>> rearrange(301302004)
    12334
    >>> rearrange(9409898038908908934890)
    33448888889999999
    '''
#一行程序 解决  牛逼
    return int("".join(sorted(str(number).replace("0", ''))))


if __name__ == '__main__':
    import doctest
    doctest.testmod()


#2018 S2 q2 
import sys
def f(n):
    '''          题目的意思是：对于某个整数表示成二进制的形式是什么，然后记录二进制当中出现1 的个数 
    >>> f(1)
    1 in binary 二进制 reads as: 1.
    Only one bit is set to 1 in the binary representation 二进制表示 of 1.              
    只有一个位置是1二进制表示1的时候
    >>> f(2)
    2 in binary reads as: 10.
    Only one bit is set to 1 in the binary representation of 2.
    >>> f(3)
    3 in binary reads as: 11.
    2 bits are set to 1 in the binary representation of 3.
    >>> f(7)
    7 in binary reads as: 111.
    3 bits are set to 1 in the binary representation of 7.
    >>> f(2314)
    2314 in binary reads as: 100100001010.
    4 bits are set to 1 in the binary representation of 2314.
    >>> f(9871)
    9871 in binary reads as: 10011010001111.
    8 bits are set to 1 in the binary representation of 9871.
    '''
    # Insert your code here

    bin_value = bin(n)[2:]         # 把 n 变成二进制的形式，注意：这里输出的bin_value 是一个字符串str 11  ==‘1011’
    count = bin_value.count('1')   #计数，所以bin_value。count 可以直接计数，count 只能用来计数str,如果得到的不是str,需要变成str才可以计数
    print(f'{n} in binary reads as: {bin_value}.')
    if count == 1:
        print(f'Only one bit is set to 1 in the binary representation of {n}.')
    else:
        print(f'{count} bits are set to 1 in the binary representation of {n}.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()

#2018 s1 q2
import sys
from math import factorial


def f(n):
    '''
    >>> f(0)                           题目的意思：先求一个整数的阶乘n_factorial，老师已经给出 n_factorial = factorial(n)
    0! is 1                            然后看这个结果（n_factorial）里面有几个3
    There is no 3 in 1
    >>> f(10)
    10! is 3628800
    There is one 3 in 3628800
    >>> f(20)
    20! is 2432902008176640000
    There is one 3 in 2432902008176640000
    >>> f(24)
    24! is 620448401733239439360000
    There are 5 3's in 620448401733239439360000
    >>> f(28)
    28! is 304888344611713860501504000000
    There are 3 3's in 304888344611713860501504000000
    >>> f(3); f(11); f(15)
    3! is 6
    There is no 3 in 6
    11! is 39916800
    There is one 3 in 39916800
    15! is 1307674368000
    There are 2 3's in 1307674368000
    '''
    if n < 0:
        sys.exit()

    n_factorial = factorial(n)     # 注意：n_factorial 是一个整数
    count = str(n_factorial).count('3')   #所以：在计数的时候把n_factorial变成 str 类型，然后才可以计数
    print(f'{n}! is {n_factorial}')
    if count == 0:
        print(f'There is no 3 in {n_factorial}')
    elif count == 1:
        print(f'There is one 3 in {n_factorial}')
    else:
        print(f"There are {count} 3's in {n_factorial}")

if __name__ == '__main__':
    import doctest
    doctest.testmod()


#2017 s1 q3
import sys
from math import factorial

def f(n):
    '''
    >>> f(0)
    0 factorial is 1      factorial 阶乘                   题目理解： 先求一个数的阶乘，找出阶乘结果中最后一个不为0的数字
    The last nonzero digit in 0 factorial is 1
    >>> f(2)
    2 factorial is 2
    The last nonzero digit in 2 factorial is 2
    >>> f(4)
    4 factorial is 24
    The last nonzero digit in 4 factorial is 4
    >>> f(10)
    10 factorial is 3628800
    The last nonzero digit in 10 factorial is 8
    >>> f(20)
    20 factorial is 2432902008176640000
    The last nonzero digit in 20 factorial is 4
    >>> f(30)
    30 factorial is 265252859812191058636308480000000
    The last nonzero digit in 30 factorial is 8
    >>> f(40)
    40 factorial is 815915283247897734345611269596115894272000000000
    The last nonzero digit in 40 factorial is 2
    '''
    value = factorial(n)   #直接求出 n 的阶乘 是value  类型是一个整数
    print(f'{n} factorial is {value}')
    for e in reversed(str(value)):
        if e !='0':  # 这里0 带有引号的意思是， 上面一步把 value翻转过来后变成了 str l类型，所以要加引号
            print(f'The last nonzero digit in {n} factorial is {e}')
            break

if __name__ == '__main__':
    import doctest
    doctest.testmod()


#2016 s2 q2
import sys
from math import factorial


def f(n):
    '''
    >>> f(0)                  题目理解：依然是先求阶乘，求出阶乘以后，判断从第一位到最后不为0的数字一共有多少位
    0 factorial is 1
    It has 1 digit, the trailing 0's excepted
    >>> f(4)
    4 factorial is 24
    It has 2 digits, the trailing 0's excepted
    >>> f(6)
    6 factorial is 720
    It has 2 digits, the trailing 0's excepted
    >>> f(10)
    10 factorial is 3628800
    It has 5 digits, the trailing 0's excepted
    >>> f(20)
    20 factorial is 2432902008176640000
    It has 15 digits, the trailing 0's excepted
    >>> f(30)
    30 factorial is 265252859812191058636308480000000
    It has 26 digits, the trailing 0's excepted
    >>> f(40)
    40 factorial is 815915283247897734345611269596115894272000000000
    It has 39 digits, the trailing 0's excepted
    '''
    if n < 0:
        sys.exit()

    n_factorial = factorial(n)

    M = 0
    lenth = len(str(n_factorial))
    
    for i in reversed(str(n_factorial)):
        if i =='0':  # 因为这里是字符串
            M +=1
        else:
            break
    number = lenth - M

    print(f'{n} factorial is {n_factorial}')

    if number != 1:
        print(f"It has {number} digits, the trailing 0's excepted")
    else:
        print(f"It has {number} digit, the trailing 0's excepted")
           # 注意 dight 当number = 1 的时候  是 dight



if __name__ == '__main__':
    import doctest
    doctest.testmod()



#lab  09  
'''
Finds all triples of positive integers (i, j, k) such that i, j and k are two digit numbers,
i < j < k, every digit occurs at most once in i, j and k, and the product of i, j and k
is a 6-digit number consisting precisely of the digits that occur in i, j and k.
找到所有正整数的三元组（i，j，k），使得i，j和k是两位数字，
i <j <k，每个数字在i，j和k中最多出现一次，并且是i，j和k的乘积
是一个6位数字，精确地包含在i，j和k中出现的数字。
'''


# If i, j and k are numbers in the range [10, 99], i < j < k, and every digit occurs at most once
# in i, j and k, then 10 <= i <= 76, j <= 87, and k <= 98. 
min_i = 10
max_i = 76
max_j = 87
max_k = 98

for i in range(min_i,max_i+1):
    i_dights = {i//10,i%10}  #// 得商（也就是取模）  % 得余数
    if len(i_dights) !=2:
        continue
    for j in range(i + 1,max_j+1):
        i_and_j_dights = i_dights.union((j//10,j%10)) #union() 方法返回两个集合的并集，
        if len(i_and_j_dights) != 4:                  #即包含了所有集合的元素，重复的元素只会出现一次
            continue
        for k in range(j+1,max_k+1):
            i_and_j_and_k_dights = i_and_j_dights.union((k//10,k%10))0
            if len(i_and_j_and_k_dights) != 6:
                continue

            product = i * j * k
            if product >=1_000_000:
                break
            if set(int(i) for i in str(product)) == i_and_j_and_k_dights:
                print(f'{i}*{j}*{k} = {product} is a solution.')

#2019 T1 Q1
#如何求一个数字所有位数的和 number=24561018  所有数字的和是多少
LL = list(int(i) for i in str(a)) # 很关键的是这个 int(i)因为for i in str(a) 得到的 i 都是str 类型
sum(LL)                           # 然后 int(i) 进行了转换 直接生成 List  让后再求和

#2019 T1 Q3
from itertools import compress,accumulate
from math import sqrt
import operator

def get_primes_3(n):
    """ Returns  a list of primes < n for n > 2 """
    if n < 2:
        return []
    if n == 2:
        return [2]
    sieve = bytearray([True]) * (n // 2)

    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = bytearray((n - i * i - 1) // (2 * i) + 1)

    return [2, *compress(range(3, n, 2), sieve[1:])]

def single_factors(number):
    '''
    Returns the product of the prime divisors of "number"
    (using each prime divisor only once).

    You can assume that "number" is an integer at least equal to 2.

    >>> single_factors(2)
    2
    >>> single_factors(4096)                 # 4096 == 2**12
    2
    >>> single_factors(85)                   # 85 == 5 * 17
    85
    >>> single_factors(10440125)             # 10440125 == 5**3 * 17**4
    85
    >>> single_factors(154)                  # 154 == 2 * 7 * 11
    154
    >>> single_factors(52399401037149926144) # 52399401037149926144 == 2**8 * 7**2 * 11**15
    154
    '''
    # return 0
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    # return
    # 11111111111111* 111111111111 =

    if number == 1:
        return 1
    elif number == 2:
        return 2
    else:

        primes = get_primes_3(10000)

        m = number
        results = set([])
        for prime in primes:
            while m!=0 and m!=1:
                a,b = divmod(m,prime)
                if b == 0:
                    results.add(prime)
                    m = a
                else:
                    break
            else:
                break

        return list(accumulate(results,func=operator.mul))[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# 2018S2-q3  素数因子

from math import sqrt
from collections import defaultdict


def f(n):
    '''                          题目理解： 把一个整数分解成 多个质数因子的乘积
    >>> f(2)
    The decomposition 分解 of 2 into prime 素数 factors 因子 reads:  将2分解成素数因子
       2 = 2
    >>> f(3)
    The decomposition of 3 into prime factors reads:
       3 = 3
    >>> f(4)
    The decomposition of 4 into prime factors reads:
       4 = 2^2
    >>> f(5)
    The decomposition of 5 into prime factors reads:
       5 = 5
    >>> f(6)
    The decomposition of 6 into prime factors reads:
       6 = 2 x 3
    >>> f(8)
    The decomposition of 8 into prime factors reads:
       8 = 2^3
    >>> f(10)
    The decomposition of 10 into prime factors reads:
       10 = 2 x 5
    >>> f(15)
    The decomposition of 15 into prime factors reads:
       15 = 3 x 5
    >>> f(100)
    The decomposition of 100 into prime factors reads:
       100 = 2^2 x 5^2
    >>> f(5432)
    The decomposition of 5432 into prime factors reads:
       5432 = 2^3 x 7 x 97
    >>> f(45103)
    The decomposition of 45103 into prime factors reads:
       45103 = 23 x 37 x 53
    >>> f(45100)
    The decomposition of 45100 into prime factors reads:
       45100 = 2^2 x 5^2 x 11 x 41
    '''
    factors = defaultdict(int)  # factors 是一个字典，生成一个字典这个字典的value 值是整数 int型
    # Insert your code here
    m = n
    for i in range(2, n + 1):
        if m == 1: 
           break
        while m % i == 0:  # m%i ==0 说明不存在余数，m 是输入的整数，一但 m%i,说明 i 就是 m 的一个因子
            factors[i] += 1  #统计个数，统计 i 的个数   i是key 对应的value +=1 (i : value)
            m = m // i       #取商

    print(f'The decomposition of {n} into prime factors reads:')
    print('  ', n, '=', end=' ')
    print(' x '.join(factors[x] == 1 and str(x) or f'{x}^{factors[x]}' for x in sorted(factors)))
     # 这个是个 乘号

if __name__ == '__main__':
    import doctest

    doctest.testmod()



#2018S1-q3   求 指定 除数因子的个数
def number_calculate(n,d):
    m = n
    count = 0
    while m!=0:
        m, a = divmod(m, d)   #divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
        if a == 0:                    #比如：divmod(7, 2)  得到 (3, 1) 这样的话 m 就会变成新的 m 商，然后继续运算下去
            count += 1
        else:
            break
    return count
        

def f(n, d):
    '''
    >>> f(2, 1)                           题目理解： n 是一个整数，目的是找 n 的所有 因子里面 包含了几个 d
    1 is not a proper 正确 factor因子 of 2.
    >>> f(2, 2)
    2 is not a proper factor of 2.
    >>> f(16, 2)
    2 is a proper  factor of 16 of mutiplicity 多重 4.
    >>> f(100, 20)          #{2,4,5,10,50,20,25}  里面只有一个20 所以
    20 is a proper factor of 100 of mutiplicity 1.
    >>> f(8 ** 7 * 3 ** 5 * 11 ** 2, 8)
    8 is a proper factor of 61662560256 of mutiplicity 7.
    >>> f(3 ** 3 * 11 * 13 ** 2 * 40 ** 6, 8)
    8 is a proper factor of 205590528000000 of mutiplicity 6.
    '''
    
    if d==1 or n == d:
        print(f'{d} is not a proper factor of {n}.')
    else:
        count = number_calculate(n , d)
        if count > 0 :
            print(f'{d} is a proper factor of {n} of mutiplicity {count}.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()

#2017S1-q4
import sys
from math import sqrt

def get_sum(n):                #求一个数字的所有 因子 的和  记住 是set
    set1 = set([1])
    for i in range(2,int(sqrt(n)) + 1):  #i 会一次遍历，直到找到所有的 因子，不仅仅是质数因子
        a,b = divmod(n,i)
        if b == 0:
            set1.add(i)   #在这里，i 是除数，a 是 商，如果余数 b ==0 ,说明 i， a 都是 n 的 因子
            set1.add(a)   #所以，这里，set1 都要加上 a , i

    return sum(set1)

def f(n):     
    '''           #求两个数字的所有因子之和,  如果和 小于 n 那么这个数就是 deficient，如果大于 n 就是 not deficient
    A number n is deficient 不足的 if the sum of its proper divisors 适当的除数,
    1 included and itself excluded,
    is strictly smaller than n.
    
    >>> f(1)
    1 is deficient
    >>> f(2)
    2 is deficient
    >>> f(3)
    3 is deficient
    >>> f(6)
    6 is not deficient
    >>> f(29)
    29 is deficient
    >>> f(30)
    30 is not deficient
    >>> f(47)
    47 is deficient
    >>> f(48)
    48 is not deficient
    '''
    #input your code
    if n == 1:
        print(f'1 is deficient')
    elif get_sum(n) <n:
        print(f'{n} is deficient')
    else:
        print(f'{n} is not deficient')



def get_sum(n):
    set1 = set([1])
    for i in range(2,int(sqrt(n)) + 1):
        a,b = divmod(n,i)
        if b == 0:
            set1.add(i)
            set1.add(a)
    return sum(set1)

def g(a, b):
    '''                            #题目理解：a 和 b 是和睦的，如果a 的所有因子加起来等于 b，b 的所有因子加起来等于a 
    a and b are amicable 和睦的 if
    - the sum of the proper divisors适当的除数 of a, 1 included and a excluded, is equal to b, and
    - the sum of the proper divisors of b, 1 included and b excluded, is equal to a.
    
    >>> g(220, 284)
    220 and 284 are amicable.
    >>> g(2924, 2620)
    2924 and 2620 are amicable.
    >>> g(1084, 1208)
    1084 and 1208 are not amicable.
    >>> g(5010, 5574)
    5010 and 5574 are not amicable.
    
    '''
    if get_sum(a) == b and get_sum(b) == a:
        print(f'{a} and {b} are amicable.')
    else:
        print(f'{a} and {b} are not amicable.')



if __name__ == '__main__':
    import doctest
    doctest.testmod()


'''  挑战完美的数字
Challenge   Perfect numbers
A number is perfect if it is equal to the sum of its divisors, 
itself excluded. For instance, the divisors of 28 distinct from 28 are 1, 2, 4, 7 and 14, 
and 1+2+4+7+14=28, hence 28 is perfect.
挑战完美的数字
如果数等于其除数的总和，则数是完美的，
本身排除在外 例如，28与28不同的除数分别为1,2,4,7和14，
并且1 + 2 + 4 + 7 + 14 = 28，因此28是完美的。
'''
import sys

try:
    N = int(input('Input an integer: ')) # 找输入的数字下面 所有的完美数
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

for i in range(2, N + 1):
    L = []
    for j in range(2, i // 2 + 1):   #%	取模 - 返回除法的余数	b % a 输出结果 0
        if i % j == 0:              #//	取整除 - 返回商的整数部分（向下取整）
            L.append(j)
    if 1 + sum(L) == i:
        print(i , 'is a perfect number')



# 2018S2-q4     求范围内的素数
import sys
from math import sqrt
from itertools import compress

# 利用byte求素数

def get_primes(n):     
    if n == 1:
        return []
    if n == 2:
        return [2]

    sieve = bytearray([True]) * (n // 2)
    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i // 2]:
            sieve[i ** 2 // 2::i] = bytearray((n - i ** 2 - 1) // (2 * i) + 1)   # ** 幂的意思
    return [2, *compress(range(3, n, 2), sieve[1:])]


def f(a, b):
    '''
    >>> f(2, 2)          求范围内的素数的个数
    There is a unique prime number beween 2 and 2.
    >>> f(2, 3)
    There are 2 prime numbers between 2 and 3.
    >>> f(2, 5)
    There are 3 prime numbers between 2 and 5.
    >>> f(4, 4)
    There is no prime number beween 4 and 4.
    >>> f(14, 16)
    There is no prime number beween 14 and 16.
    >>> f(3, 20)
    There are 7 prime numbers between 3 and 20.
    >>> f(100, 800)
    There are 114 prime numbers between 100 and 800.
    >>> f(123, 456789)
    There are 38194 prime numbers between 123 and 456789.
    >>> f(24, 78)
    There are 12 prime numbers between 24 and 78.
    >>> f(11, 56)
    There are 12 prime numbers between 11 and 56.
    >>> f(23, 534)
    There are 91 prime numbers between 23 and 534.
    >>> f(34, 3463)
    There are 474 prime numbers between 34 and 3463.
    >>> f(143, 342)
    There are 34 prime numbers between 143 and 342.
    >>> f(234, 457)
    There are 37 prime numbers between 234 and 457.
    >>> f(1000, 3434)
    There are 313 prime numbers between 1000 and 3434.
    >>> f(8933, 23414)
    There are 1497 prime numbers between 8933 and 23414.
    >>> f(2342, 235235)
    There are 20505 prime numbers between 2342 and 235235.
    >>> f(235, 3423524)
    There are 245064 prime numbers between 235 and 3423524.
    >>> f(9984, 232454)
    There are 19404 prime numbers between 9984 and 232454.
    >>> f(234554, 3423523)
    There are 224321 prime numbers between 234554 and 3423523.
    >>> f(909812, 2312414)
    There are 98351 prime numbers between 909812 and 2312414.
    >>> f(324235, 3253463)
    There are 205866 prime numbers between 324235 and 3253463.
    >>> f(3, 3125563)
    There are 225208 prime numbers between 3 and 3125563.
    >>> f(555, 5555555)
    There are 384225 prime numbers between 555 and 5555555.
    >>> f(32423, 456346)
    There are 34706 prime numbers between 32423 and 456346.
    >>> f(1, 1232553)
    There are 95235 prime numbers between 1 and 1232553.
    >>> f(9834, 435546)
    There are 35394 prime numbers between 9834 and 435546.
    >>> f(23, 4461224)
    There are 313395 prime numbers between 23 and 4461224.
    >>> f(234235, 5645747)
    There are 369351 prime numbers between 234235 and 5645747.
    >>> f(145667, 7834134)
    There are 515821 prime numbers between 145667 and 7834134.
    >>> f(672342, 9341232)
    There are 569234 prime numbers between 672342 and 9341232.
    >>> f(7823045, 9079934)
    There are 78780 prime numbers between 7823045 and 9079934.
    >>> f(13, 9998734)
    There are 664503 prime numbers between 13 and 9998734.
    '''
    number_of_primes_at_most_equal_to_b = 0  # 素数的 个数
    # Insert your code here
    primes_a = get_primes(a)    # 调用 get_primes 函数 直接求出  a 所有的素数
    primes = get_primes(b + 1)  # 调用 get_primes 函数 直接求出  b+1 所有的素数
    number_of_primes_at_most_equal_to_b = len(primes) - len(primes_a)   #利用长度相减 得出 在a b 之间 有几个数字

    if a in primes_a:
        number_of_primes_at_most_equal_to_b += 1

    if b + 1 in primes:
        number_of_primes_at_most_equal_to_b -= 1

    if not number_of_primes_at_most_equal_to_b:
        print(f'There is no prime number beween {a} and {b}.')
    elif number_of_primes_at_most_equal_to_b == 1:
        print(f'There is a unique prime number beween {a} and {b}.')
    else:
        print(f'There are {number_of_primes_at_most_equal_to_b} prime numbers between {a} and {b}.')



if __name__ == '__main__':
    import doctest
    doctest.testmod()



# 2017S1-q5  求范围内的素数
import sys
from math import sqrt
from itertools import compress

def get_primes(n):     
    if n < 2:
        return []
    if n == 2:
        return [2]

    sieve = bytearray([True]) * (n // 2)
    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i // 2]:
            sieve[i ** 2 // 2::i] = bytearray((n - i ** 2 - 1) // (2 * i) + 1)   # ** 幂的意思
    return [2, *compress(range(3, n, 2), sieve[1:])]

def f(a, b):
    '''
    Won't be tested for b greater than 10_000_000   求范围内的素数
    
    >>> f(3, 3)
    The number of prime numbers between 3 and 3 included is 1
    >>> f(4, 4)
    The number of prime numbers between 4 and 4 included is 0
    >>> f(2, 5)
    The number of prime numbers between 2 and 5 included is 3
    >>> f(2, 10)
    The number of prime numbers between 2 and 10 included is 4
    >>> f(2, 11)
    The number of prime numbers between 2 and 11 included is 5
    >>> f(1234, 567890)
    The number of prime numbers between 1234 and 567890 included is 46457
    >>> f(89, 5678901)
    The number of prime numbers between 89 and 5678901 included is 392201
    >>> f(89, 5678901)
    The number of prime numbers between 89 and 5678901 included is 392201
    '''
    primes = get_primes(b + 1)
    count = 0
    for item in primes:
        if a <= item <= b:
            count += 1
    print(f'The number of prime numbers between {a} and {b} included is {count}')


if __name__ == '__main__':
    import doctest
    doctest.testmod()


#2016 s2 - q3 求两个整数之间 所有素数之间的最大间隔
import sys
from math import sqrt

def is_prime(n):  #判断n 是不是质数
    if n ==1:
        return False
    up_bound = round(sqrt(n))+1
    for i in range(2,up_bound):
        if n % i ==0:
            return False
    return True

def f(a, b):
    '''              先求一个整数的素数，然后求素数的间隔，找出最大的间隔
    The prime numbers between 2 and 12 (both included) are: 2, 3, 5, 7, 11
    The gaps between successive primes are: 0, 1, 1, 3.
    Hence the maximum gap is 3.
    
    Won't be tested for b greater than 10_000_000
    
    >>> f(3, 3)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 4)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 5)
    The maximum gap between successive prime numbers in that interval is 1
    >>> f(2, 12)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(5, 23)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(20, 106)
    The maximum gap between successive prime numbers in that interval is 7
    >>> f(31, 291)
    The maximum gap between successive prime numbers in that interval is 13
    '''
    if a <= 0 or b < a:
        sys.exit()
    max_gap = 0
    
    list_of_prime = []
    for i in range(a, b + 1):
        if is_prime(i):
            list_of_prime.append(i)  #构建两个数之间的质数序列


    if len(list_of_prime) == 1 or len(list_of_prime) == 0: #极端情况
        print('The maximum gap between successive prime numbers in that interval is 0')
    
    else:
        max_gap = list_of_prime[1] - list_of_prime[0]
        list_of_prime.sort() 
        
        for i in range(len(list_of_prime) - 1): #需要测试几次，求几次间隙
            if list_of_prime[i+1] - list_of_prime[i] >= max_gap:
                max_gap = list_of_prime[i+1] - list_of_prime[i]
                # 11 -7 =4 但是间隔是3 所以下面 -=1
                max_gap -= 1  
        print(f'The maximum gap between successive prime numbers in that interval is {max_gap}')

if __name__ == '__main__':
    import doctest
    doctest.testmod()


# 2018S1-q4  求距离最近的素数
import sys
from math import sqrt
from itertools import compress

def get_primes(n):     
    if n < 2:
        return []
    if n == 2:
        return [2]

    sieve = bytearray([True]) * (n // 2)
    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i // 2]:
            sieve[i ** 2 // 2::i] = bytearray((n - i ** 2 - 1) // (2 * i) + 1)   # ** 幂的意思
    return [2, *compress(range(3, n, 2), sieve[1:])]


def f(n):
    '''        # 求距比  n  小的最大的素数 
    Won't be tested for n greater than 10_000_000
    
    >>> f(3)
    The largest prime strictly smaller than 3 is 2.
    >>> f(10)
    The largest prime strictly smaller than 10 is 7.
    >>> f(20)
    The largest prime strictly smaller than 20 is 19.
    >>> f(210)
    The largest prime strictly smaller than 210 is 199.
    >>> f(1318)
    The largest prime strictly smaller than 1318 is 1307.
    '''
    if n <= 2:
        sys.exit()
    largest_prime_strictly_smaller_than_n = 0
    # Insert your code here
    if n = 3:
        print(f'The largest prime strictly smaller than 3 is 2.')
    else:
        primes = get_primes(n)
        largest_prime_strictly_smaller_than_n = max(primes)
        print(f'The largest prime strictly smaller than {n} is {largest_prime_strictly_smaller_than_n}.')


if __name__ == '__main__':
    import doctest
    doctest.testmod()


##############################################################################
#乘法计算

#2019 s1pre  Q 7
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


def subnumbers_whose_digits_add_up_to_ext(number, sum_of_digits ,current_result,results):
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    # 123456     11 - 6 -5 == 0
    if number >= 0:
        if sum_of_digits == 0:
            results.add(current_result)
            return
    # 如果number = 2,sum of digits = 2
    if number == sum_of_digits:
        results.add(current_result * 10 + number)
        return
    # sum of digits = -1 or number == 0
    if sum_of_digits < 0 or number == 0:
        return

    a, b = divmod(number, 10)
    # a = 123,b =4
    subnumbers_whose_digits_add_up_to_ext(a, sum_of_digits - b,current_result * 10 + b,results)
    subnumbers_whose_digits_add_up_to_ext(a, sum_of_digits,current_result,results)

    # subnumbers_whose_digits_add_up_to(1234, 5)
    #               None
    # Nne                           1
    #  None, 2                  None,           2
    #   None,3  None,3           None,    3       None,   3


# POSSIBLY DEFINE OTHER


# POSSIBLY DEFINE OTHER

def subnumbers_whose_digits_add_up_to(number, sum_of_digits):
    '''
    You can assume that "number" consists of digits not equal to 0
    and that "sum_of_digits" is an integer.

    A solution is obtained by possibly deleting some digits in "number"
    (keeping the order of the remaining digits) so that the sum of
    of the remaining digits is equal to "sum_of_digits".

    The solutions are listed from smallest to largest, with no duplicate.

    >>> subnumbers_whose_digits_add_up_to(13, 2)
    []
    >>> subnumbers_whose_digits_add_up_to(222, 2)
    [2]
    >>> subnumbers_whose_digits_add_up_to(123, 6)
    [123]
    >>> subnumbers_whose_digits_add_up_to(222, 4)
    [22]
    >>> subnumbers_whose_digits_add_up_to(1234, 5)
    [14, 23]
    >>> subnumbers_whose_digits_add_up_to(12341234, 4)
    [4, 13, 22, 31, 112, 121]
    >>> subnumbers_whose_digits_add_up_to(121212, 5)
    [122, 212, 221, 1112, 1121, 1211]
    >>> subnumbers_whose_digits_add_up_to(123454321, 10)
    [145, 154, 235, 244, 253, 343, 352, 442, 451, 532, 541, 1234, 1243, \
1252, 1342, 1351, 1432, 1441, 1531, 2332, 2341, 2431, 2521, 3421, \
4321, 12331, 12421, 13321]
    '''

    results = set([])
    subnumbers_whose_digits_add_up_to_ext(int(str(number)[::-1]), sum_of_digits, 0,results)
    return sorted(results)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # print(subnumbers_whose_digits_add_up_to(123, 6))
    # print(sorted(subnumbers_whose_digits_add_up_to(123454321, 10)))

# 2017S1-q6  计算两个乘法都只出现一次数字
import sys

def f(a, b):
    '''
    Finds all numbers i and j with a <= i <= j <= b such that
    every digit occurs at most once in i, j and i * j.
    Outputs the solutions from smallest i to largest i,
    and for a given i from smallest j to largest j.
    查找所有数字i和j，其中a <= i <= j <= b
    在i，j和i * j中，每个数字最多出现一次。
    输出从最小i到最大i的解决方案，
    对于给定的i，从最小的j到最大的j。
    
    >>> f(32, 49)
    32 * 49 = 1568 is a solution
    38 * 42 = 1596 is a solution
    >>> f(30, 50)
    32 * 49 = 1568 is a solution
    38 * 42 = 1596 is a solution
    >>> f(40, 80)
    48 * 65 = 3120 is a solution
    52 * 79 = 4108 is a solution
    53 * 76 = 4028 is a solution
    58 * 64 = 3712 is a solution
    59 * 68 = 4012 is a solution
    59 * 78 = 4602 is a solution
    68 * 74 = 5032 is a solution
    >>> f(50, 110)
    52 * 79 = 4108 is a solution
    53 * 76 = 4028 is a solution
    53 * 92 = 4876 is a solution
    57 * 86 = 4902 is a solution
    58 * 64 = 3712 is a solution
    59 * 68 = 4012 is a solution
    59 * 78 = 4602 is a solution
    59 * 108 = 6372 is a solution
    62 * 87 = 5394 is a solution
    68 * 74 = 5032 is a solution
    69 * 108 = 7452 is a solution
    72 * 95 = 6840 is a solution
    74 * 85 = 6290 is a solution
    '''
    for i in range(a,b+1):
        for j in range(i,b+1):
            value = i*j
            if len(str(i)) + len(str(j)) + len(str(value)) == len(set(str(i) + str(j) + str(value))):
                print(f'{i} * {j} = {value} is a solution')

if __name__ == '__main__':
    import doctest
    doctest.testmod()


# 2016S2-q5  计算升序+降序等于中间值


#lab07两个数相乘的计算
'''
Decodes all multiplications of the form

                       *  *  *
                  x       *  *
                    ----------
                    *  *  *  *
                    *  *  *
                    ----------
                    *  *  *  *

such that the sum of all digits in all 4 columns is constant.
##Decoding一个乘法
#We想要解码表单的所有乘法
#such，所有4列中所有数字的总和是不变的。
'''
for i in range(100,1000):  #取第一个三位数，遍历 100 到1000之间
    for j in range(10,100): #取第一个二位数，遍历 10 到100之间
        first_outcome = i *(j % 10) #进行乘法，j的个位乘以i
        if not 1000 <= first_outcome <=9999:
            continue  # 会直接跳出这个循环返回小循环继续执行
        second_outcome = i *(j // 10) #进行乘法，j的十位乘以i
        if not 100 <= second_outcome <999:
            continue
        final_outcome = first_outcome + 10*second_outcome #得出最终的结果
        if not 1000 <= final_outcome <= 9999: #判断是否为4位数
            continue
        #因为在题目中要求四列加起来的值要相等
        sum_col1 = int(str(i)[-1]) + int(str(j)[-1])\
                    + int(str(first_outcome)[-1]) + int(str(final_outcome)[-1])
        sum_col2 = int(str(i)[-2]) + int(str(j)[-2])\
                    + int(str(first_outcome)[-2]) + int(str(second_outcome)[-1])\
                    + int(str(final_outcome)[-2])
        sum_col3 = int(str(i)[-3]) + int(str(first_outcome)[-3]) + int(str(second_outcome)[-2])\
                    + int(str(final_outcome)[-3])
        sum_col4 = int(str(first_outcome)[0]) + int(str(second_outcome)[0])\
                    + int(str(final_outcome)[0])
        if sum_col1 == sum_col2 == sum_col3 == sum_col4:
            print(f"{i}*{j} = {final_outcome},all columns adding to {sum_col1}.")


#lab04   平均数，中位数，标准差




# Fibonacci
def fibonacci_numbers_up_to_n(n):
    previous = 1
    current = 1
    numbers = []
    while current <= n:
        numbers.append(current)
        previous, current = current, previous + current
    return numbers

##############################################################################

#字符串操作 
# 2019 s1-prefer Q 5
def longest_leftmost_sequence_of_consecutive_letters(word):
    '''
    You can assume that "word" is a string of
    nothing but lowercase letters.

    >>> longest_leftmost_sequence_of_consecutive_letters('')
    ''
    >>> longest_leftmost_sequence_of_consecutive_letters('a')
    'a'
    >>> longest_leftmost_sequence_of_consecutive_letters('zuba')
    'z'
    >>> longest_leftmost_sequence_of_consecutive_letters('ab')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('bcab')
    'bc'
    >>> longest_leftmost_sequence_of_consecutive_letters('aabbccddee')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('aefbxyzcrsdt')
    'xyz'
    >>> longest_leftmost_sequence_of_consecutive_letters('efghuvwijlrstuvabcde')
    'rstuv'
    '''
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE

    max_string = ''
    if word:
        first = word[0]
        max_length = 1
        temp_length = 1
        max_string = first
        temp_string = first
        # ab
        #
        for second in word[1:]:
            if ord(first) + 1 == ord(second):
                temp_length += 1
                temp_string += second
            else:
                max_length = max(max_length, temp_length)
                if len(temp_string) > len(max_string):
                    max_string = temp_string
                temp_length = 1
                temp_string = second

            first = second

        max_length = max(max_length, temp_length)

        if len(temp_string) > len(max_string):
            max_string = temp_string

    return max_string


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# 2018S2-q2  求1的个数，与整数操作里面的求一个数字的除数，余数相同）
字符串操作
#2018S1-q5 求从左侧开始，向右最长的字符串
def f(word):
    '''       ############  字符串操作
    Recall that if c is an ascii character then ord(c) returns its ascii code.
    Will be tested on nonempty strings of lowercase letters only.
    回想一下，如果c是ascii字符，则ord（c）返回其ascii代码。
     将仅在非空字符串的小写字母上进行测试。

    >>> f('x')
    The longest substring of consecutive letters has a length of 1.
    连续字母的最长子字符串长度为1
    The leftmost such substring is x.
    最左边的这个子串是x
    >>> f('xy')
    The longest substring of consecutive letters has a length of 2.
    The leftmost such substring is xy.
    >>> f('ababcuvwaba')
    The longest substring of consecutive letters has a length of 3.
    The leftmost such substring is abc.
    >>> f('abbcedffghiefghiaaabbcdefgg')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is bcdefg.
    >>> f('abcabccdefcdefghacdef')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is cdefgh.
    '''
    desired_length = 0   #desired length  期望的长度
    desired_substring = ''  #期望的子串  期望的子串
    # Insert your code here
    if word:  #word 在这里是一个字符串，所以后面的操作可以 直接取它的第几位
        desired_length = 1
        temp_substring = word[0] #临时子串 等于 word 的第0位，也就是第一个字母
        temp_length = 1          #临时长度，
        for i in range(1,len(word)):
            if ord(temp_substring[-1]) + 1 == ord(word[i]):  #临时子串的最后一位，转为ord() 数字 + 1 = 后面一位， 说明是连续的
                temp_substring += word[i]   #那么就把这一位 加入到临时子串里面
                temp_length +=1           #临时子串的 长度 +1 
            else:  # 如果当前位置 +1 不等于后面一位，就是不连续的情况
                desired_length = max(temp_length,desired_length)  #返回临时长度 和 期望长度里面的最大值
                if len(temp_substring) > len(desired_substring): # 如果临时子串的长度 大于 期望长度的子串
                    desired_substring = temp_substring          #更新期望长度

                temp_length = 1  #这里是重置，临时长度 变回1
                temp_substring = word[i]      # 临时子串 变成word[i]
                
        desired_length = max(temp_length,desired_length) #
        if len(temp_substring) > len(desired_substring):
            desired_substring = temp_substring
    print(f'The longest substring of consecutive letters has a length of {desired_length}.')
    print(f'The leftmost such substring is {desired_substring}.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()

2018  s2  final 1


from itertools import groupby

def remove_consecutive_duplicates(word):
    # 删除连续的重复项
    '''
    >>> remove_consecutive_duplicates('')
    ''
    >>> remove_consecutive_duplicates('a')
    'a'
    >>> remove_consecutive_duplicates('ab')
    'ab'
    >>> remove_consecutive_duplicates('aba')
    'aba'
    >>> remove_consecutive_duplicates('aaabbbbbaaa')
    'aba'
    >>> remove_consecutive_duplicates('abcaaabbbcccabc')
    'abcabcabc'
    >>> remove_consecutive_duplicates('aaabbbbbaaacaacdddd')
    'abacacd'
    '''
    # Insert your code here (the output is returned, not printed out)
    result = ''
    if word:
        result = word[0]
        for char in word[1:]:
            if result[-1] != char:
                result += char

    return result



'''
Given a word w, a good subsequence of w is defined as a word w' such that
- all letters in w' are different;
- w' is obtained from w by deleting some letters in w.

Returns the list of all good subsequences, without duplicates, in lexicographic order
(recall that the sorted() function sorts strings in lexicographic order).

The number of good sequences grows exponentially in the number of distinct letters in w,
so the function will be tested only for cases where the latter is not too large.

'''

from itertools import combinations, groupby

2018  s2  final 3
def good_subsequences(word):
    '''
    >>> good_subsequences('')
    ['']
    >>> good_subsequences('aaa')
    ['', 'a']
    >>> good_subsequences('aaabbb')
    ['', 'a', 'ab', 'b']
    >>> good_subsequences('aaabbc')
    ['', 'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
    >>> good_subsequences('aaabbaaa')
    ['', 'a', 'ab', 'b', 'ba']
    >>> good_subsequences('abbbcaaabccc')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb']
    >>> good_subsequences('abbbcaaabcccaaa')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    >>> good_subsequences('abbbcaaabcccaaabbbbbccab')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    '''
    result = ['']
    if word:
        # first method
        for x in word:
            letters = set(result)
            for item in result:
                if x not in item:
                    value = item + x
                    letters.add(value)
                else:
                    value = item.replace(x, '') + x  #把x 替换成 '' 空 再把x 加在上面0
                    letters.add(value)

            result = list(letters)

        # second method
        words = [k for k, g in groupby(word)]
        result = set(
            [''.join(item)
             for i in range(len(set(words)) + 1)
             for item in combinations(words, i) if
             len(item) == len(set(item))])

    return sorted(result)


# Possibly define another function


if __name__ == '__main__':
    import doctest

    doctest.testmod()
###############################################################################################################
#列表操作


# 2018 S1-q2  final pre
def rearrange(L, from_first = True):
    '''
    Returns a new list consisting of:
    * in case "from_first" is True:
         L's first member if it exists, then
         L's last member if it exists, then
         L's second member if it exists, then
         L's second last member if it exists, then
         L's third member if it exists...
    * in case "from_first" is False:
         L's last member if it exists, then
         L's first member if it exists, then
         L's second last member if it exists, then
         L's second member if it exists, then
         L's third last member if it exists...

    >>> L = []
    >>> rearrange(L), L
    ([], [])
    >>> L = [10]
    >>> rearrange(L, False), L
    ([10], [10])
    >>> L = [10, 20]
    >>> rearrange(L), L
    ([10, 20], [10, 20])
    >>> L = [10, 20, 30]
    >>> rearrange(L), L
    ([10, 30, 20], [10, 20, 30])
    >>> L = [10, 20, 30, 40]
    >>> rearrange(L, False), L
    ([40, 10, 30, 20], [10, 20, 30, 40])
    >>> L = [10, 20, 30, 40, 50]
    >>> rearrange(L, False), L
    ([50, 10, 40, 20, 30], [10, 20, 30, 40, 50])
    >>> L = [10, 20, 30, 40, 50, 60]
    >>> rearrange(L), L
    ([10, 60, 20, 50, 30, 40], [10, 20, 30, 40, 50, 60])
    >>> L = [10, 20, 30, 40, 50, 60, 70]
    >>> rearrange(L), L
    ([10, 70, 20, 60, 30, 50, 40], [10, 20, 30, 40, 50, 60, 70])
    '''
    # return []
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    #
    result = []
    if L:
        if from_first:  #from_first== True 的情况第一个，最后一个，第二个，倒数第二个，第三个，倒数第三个,
            for index in range(len(L)):
                # index  = 2
                # a = 1
                a, b = divmod(index, 2)
                # 奇数
                # 偶数
                #     >>> L = [10, 20, 30]
                #     >>> rearrange(L), L
                #     ([10, 30, 20], [10, 20, 30])
                # index  = 0, 1，2
                if b == 0:
                    result.append(L[a])
                # index  = 1
                else:
                    # index = 1,a = 0,b = 1
                    result.append(L[0 - (a + 1)])

        else:  #from_first== False 的情况：最后一个，第一个,第二个，倒数第二个，第三个，单数第三个
            for index in range(len(L)):
                # index  = 2
                # a = 1
                a, b = divmod(index, 2)
                # 奇数
                # 偶数
                #     >>> L = [10, 20, 30]
                #     >>> rearrange(L), L
                #     ([10, 30, 20], [10, 20, 30])
                # index  = 0, 2
                if b == 0:
                    # index = 0,a = 0,b = 0
                    # index = 2 a = 1,b = 0
                    result.append(L[0 - (a + 1)])
                # index  = 1
                else:
                    # index = 1,a = 0,b = 1
                    #
                    result.append(L[a])
    return result

    result = []
    if L:
        if from_first:  #from_first== True 的情况第一个，最后一个，第二个，倒数第二个，第三个，倒数第三个,
            for index in range(len(L)):
                a, b = divmod(index, 2)
                if b == 0:
                    result.append(L[a])
                else:
                    result.append(L[0 - (a + 1)])

        else:  #from_first== False 的情况：最后一个，第一个,第二个，倒数第二个，第三个，单数第三个
            for index in range(len(L)):
                a, b = divmod(index, 2)
                if b == 0:
                    result.append(L[0 - (a + 1)])
                else:
                    result.append(L[a])
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
# 2018S2-q1   2016S2-q1   求连续的不重复的升序列表      （分割列表，求不重复的升序）

from random import seed, randint
import sys


def f(arg_for_seed, nb_of_elements, max_element):
    '''
    >>> f(0, 0, 10)      求连续的不重复的升序列表
    Here is L: []
    The decomposition of L into increasing sequences,  将L分解为递增序列，连续重复删除
        with consecutive duplicates removed, is:
        []
    >>> f(0, 1, 10)
    Here is L: [6]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6]]
    >>> f(0, 2, 10)
    Here is L: [6, 6]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6]]
    >>> f(0, 3, 10)
    Here is L: [6, 6, 0]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6], [0]]
    >>> f(0, 4, 10)
    Here is L: [6, 6, 0, 4]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6], [0, 4]]
    >>> f(0, 5, 10)
    Here is L: [6, 6, 0, 4, 8]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6], [0, 4, 8]]
    >>> f(0, 6, 10)
    Here is L: [6, 6, 0, 4, 8, 7]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6], [0, 4, 8], [7]]
    >>> f(0, 7, 10)
    Here is L: [6, 6, 0, 4, 8, 7, 6]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6], [0, 4, 8], [7], [6]]
    >>> f(3, 10, 6)
    Here is L: [1, 4, 4, 1, 2, 4, 3, 5, 4, 0]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[1, 4], [1, 2, 4], [3, 5], [4], [0]]
    >>> f(3, 15, 8)
    Here is L: [3, 8, 2, 5, 7, 1, 0, 7, 4, 8, 3, 3, 7, 8, 8]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[3, 8], [2, 5, 7], [1], [0, 7], [4, 8], [3, 7, 8]]
    '''
    if nb_of_elements < 0:  #如果取得数字小于0，退出
        sys.exit()
    seed(arg_for_seed)
    L = [randint(0, max_element) for _ in range(nb_of_elements)]  #生成L
    print('Here is L:', L)
    
    R = []
    
    if L:
        R.append([L[0]])  # R 中加入 L[0]
        for x in L[1:]:   #这里  x  是一个整数
            if x > R[-1][-1]: #如果 x > R 列表最后一个列表元素（也是个列表）里面的最后一位（是一个数字），说明递增
                R[-1].append(x)   # 那么就把x 加入到 R 列表最后一个列表里面
            elif x == R[-1][-1]: #如果 相等
                continue
            else:
                R.append([x])
    print('The decomposition of L into increasing sequences,')
    print('    with consecutive duplicates removed, is:\n   ', R)


if __name__ == '__main__':
    import doctest
    doctest.testmod()


from random import seed, randint
import sys


def f(arg_for_seed, nb_of_elements, max_element):
    '''
    >>> f(0, 0, 10)
    Here is L: []
    The decomposition of L into increasing sublists is: []
    >>> f(0, 1, 10)
    Here is L: [6]
    The decomposition of L into increasing sublists is: [[6]]
    >>> f(0, 2, 10)
    Here is L: [6, 6]
    The decomposition of L into increasing sublists is: [[6], [6]]
    >>> f(1, 2, 10)
    Here is L: [2, 9]
    The decomposition of L into increasing sublists is: [[2, 9]]
    >>> f(0, 3, 10)
    Here is L: [6, 6, 0]
    The decomposition of L into increasing sublists is: [[6], [6], [0]]
    >>> f(1, 4, 10)
    Here is L: [2, 9, 1, 4]
    The decomposition of L into increasing sublists is: [[2, 9], [1, 4]]
    >>> f(20, 5, 10)
    Here is L: [10, 2, 4, 10, 10]
    The decomposition of L into increasing sublists is: [[10], [2, 4, 10], [10]]
    >>> f(1, 10, 20)
    Here is L: [4, 18, 2, 8, 3, 15, 14, 15, 20, 12]
    The decomposition of L into increasing sublists is: [[4, 18], [2, 8], [3, 15], [14, 15, 20], [12]]
    '''
    if nb_of_elements < 0:
        sys.exit()
    seed(arg_for_seed)
    L = [randint(0, max_element) for _ in range(nb_of_elements)]
    print('Here is L:', L)
    R = []
    # Insert your code here
    if L == []:
        print(f'The decomposition of L into increasing sublists is: []')
    else:
        R.append([L[0]])  # R 中加入 L[0]
        for x in L[1:]:   #这里  x  是一个整数
            if x > R[-1][-1]: #如果 x > R 列表最后一个列表元素（也是个列表）里面的最后一位（是一个数字），说明递增
                R[-1].append(x)   # 那么就把x 加入到 R 列表最后一个列表里面  
            else:
                R.append([x])
        print(f'The decomposition of L into increasing sublists is: {R}')    

if __name__ == '__main__':
    import doctest
    doctest.testmod()


#2018S1-q1  求偶数子列表
from random import seed, randint
import sys


def f(arg_for_seed, nb_of_elements, max_element):
    '''
    >>> f(0, 0, 10)
    Here is L: []
    The decomposition of L into longest sublists子列表 of even numbers 偶数 is: []
    >>> f(0, 1, 10)
    Here is L: [6]
    The decomposition of L into longest sublists of even numbers is: [[6]]
    >>> f(0, 2, 10)
    Here is L: [6, 6]
    The decomposition of L into longest sublists of even numbers is: [[6, 6]]
    >>> f (0, 2, 2)
    Here is L: [1, 1]
    The decomposition of L into longest sublists of even numbers is: []
    >>> f(1, 2, 10)
    Here is L: [2, 9]
    The decomposition of L into longest sublists of even numbers is: [[2]]
    >>> f(1, 4, 10)
    Here is L: [2, 9, 1, 4]
    The decomposition of L into longest sublists of even numbers is: [[2], [4]]
    >>> f(1, 8, 8)
    Here is L: [2, 1, 4, 1, 7, 7, 7, 6]
    The decomposition of L into longest sublists of even numbers is: [[2], [4], [6]]
    >>> f(1, 10, 20)
    Here is L: [4, 18, 2, 8, 3, 15, 14, 15, 20, 12]
    The decomposition of L into longest sublists of even numbers is: [[4, 18, 2, 8], [14], [20, 12]]
    '''
    if nb_of_elements < 0:
        sys.exit()
    seed(arg_for_seed)
    L = [randint(0, max_element) for _ in range(nb_of_elements)]
    print('Here is L:', L)
    R = []

    new_set = []  #相当于 new_set  是 R 中的 一个子列表
    for e in L:
        if e % 2 == 0:  #判断是否是偶数
             new_set.append(e)
        else:
            if new_set:
                R.append(new_set)
            new_set = []
    if new_set:
        R.append(new_set)
    # Insert your code here
    print('The decomposition of L into longest sublists of even numbers is:', R)    


if __name__ == '__main__':
    import doctest
    doctest.testmod()

#2018S2-q6 列表翻转          列表排序，翻转,numpy



# 2017S1-q1  列表排序 列表去绝对值最小值，并且排序

from random import seed, randint
import sys

def f(arg_for_seed, nb_of_elements, max_element):
    '''
    >>> f(0, 0, 10)
    Here is L: []
    The second smallest element in L is: None
    The minimum gap in absolute value between successive 连续的 elements in L is: 0
    >>> f(0, 1, 10)
    Here is L: [6]
    The second smallest element in L is: None
    The minimum gap in absolute value between successive elements in L is: 0
    >>> f(0, 2, 10)
    Here is L: [6, 6]
    The second smallest element in L is: None
    The minimum gap in absolute value between successive elements in L is: 0
    >>> f(1, 2, 10)
    Here is L: [2, 9]
    The second smallest element in L is: 9
    The minimum gap in absolute value between successive elements in L is: 7
    >>> f(0, 3, 10)
    Here is L: [6, 6, 0]
    The second smallest element in L is: 6
    The minimum gap in absolute value between successive elements in L is: 0
    >>> f(1, 4, 10)
    Here is L: [2, 9, 1, 4]
    The second smallest element in L is: 2
    The minimum gap in absolute value between successive elements in L is: 3
    >>> f(20, 5, 10)
    Here is L: [10, 2, 4, 10, 10]
    The second smallest element in L is: 4
    The minimum gap in absolute value between successive elements in L is: 0
    >>> f(1, 10, 20)
    Here is L: [4, 18, 2, 8, 3, 15, 14, 15, 20, 12]
    The second smallest element in L is: 3
    The minimum gap in absolute value between successive elements in L is: 1
    '''
    seed(arg_for_seed)
    L = [randint(0,max_element) for _ in range(nb_of_elements)]
    print ('Here is L:',L)


    if len(L) < 2:  #处理边缘情况
        print('The second smallest element in L is: None')
        print(f'The minimum gap in absolute value between successive elements in L is: 0')


    else:
        min_gap = abs(L[1] - L[0])  # abs() 求绝对值
        for i in range(2,len(L)):
            min_gap = min(min_gap,abs(L[i] - L[i-1]))

        # 开始求 The second smallest element ，思路： 先排序stored(L), 取排序完列表的第一个值start，然后遍历，如果下一个值 >  start， 
        index = 1     #把　e 的值 付给 start .index +=1,如果Index 的值大于2，就break
        new_L = sorted(L)
        start = new_L[0]
        for e in new_L:
            if e > start:
                index +=1
                start = e
                if index >=2:
                    break
        if index ==2:
            print(f'The second smallest element in L is: {start}')
        else:
            print('The second smallest element in L is: None')
        print(f'The minimum gap in absolute value between successive elements in L is: {min_gap}')
    
 

    

if __name__ == '__main__':
    import doctest
    doctest.testmod()



# 列表遍历 
#2017S1-q2
from random import seed, randint
import sys

def f(arg_for_seed, nb_of_elements, max_element):
    '''
    >>> f(0, 0, 10)    列表遍历
    Here is L: []
    >>> f(0, 1, 10)
    Here is L: [6]
    1 element starts with 6
    >>> f(0, 2, 10)
    Here is L: [6, 6]
    2 elements start with 6
    >>> f(1, 2, 100)
    Here is L: [17, 72]
    1 element starts with 1
    1 element starts with 7
    >>> f(2, 3, 1000)
    Here is L: [978, 883, 970]
    1 element starts with 8
    2 elements start with 9
    >>> f(8, 6, 1000)
    Here is L: [232, 379, 985, 384, 129, 197]
    2 elements start with 1
    1 element starts with 2
    2 elements start with 3
    1 element starts with 9
    >>> f(20, 8, 10000)
    Here is L: [2477, 4257, 1663, 5364, 9387, 2775, 442, 6742]
    1 element starts with 1
    2 elements start with 2
    2 elements start with 4
    1 element starts with 5
    1 element starts with 6
    1 element starts with 9
    '''
    seed(arg_for_seed)
    L = [randint(0,max_element) for _ in range(nb_of_elements)]
    print ('Here is L:',L)
    if L:
        new_list = [0] * 9  # 结果为 [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for e in L:  #遍历 L 中的每一个元素，然后把 e 变成字符串 取第 0 位，再转变为 int 类型 ， 再减去1 表示  new_list 的index 值
            new_list[int(str(e)[0]) - 1] +=1   # 一但进入循环，肯定该位置上有数字。计算个数
            
        for i in range(0,9): #遍历 new_list的每一位，看看每个位置上面的数字是几
            if new_list[i] > 1:
                print(f'{new_list[i]} elements start with {i+1}')
            elif new_list[i]:
                print(f'{new_list[i]} element starts with {i+1}')


if __name__ == '__main__':
    import doctest
    doctest.testmod()

###########################################################################################################


#lab02  #求最大最小值
'''
Prompts the user for a seed for the random number generator,
and for a strictly positive number, nb_of_elements.
Generates a list of nb_of_elements random integers between 0 and 99, prints out the list,
computes the difference between the largest and smallest values in the list without using
the builtins min() and max(), prints it out, and check that the result is correct using
the builtins.
提示用户输入随机数生成器的种子，
并且对于严格正数，nb_of_elements。
生成0到99之间的nb_of_elements随机整数列表，打印出列表，
在不使用的情况下计算列表中最大值和最小值之间的差异
内置的min（）和max（），打印出来，并使用确认结果是否正确
内置的。
'''

#求最大最小值

from random import seed, randint
import sys


# Prompts the user for a seed for the random number generator,
# and for a strictly positive number, nb_of_elements.
try:
    arg_for_seed = int(input('Input a seed for the random number generator: '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()   
try:
    nb_of_elements = int(input('How many elements do you want to generate? '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()
# Generates a list of nb_of_elements random integers between 0 and 99.
seed(arg_for_seed)
L = [randint(0, 99) for _ in range(nb_of_elements)]
# Prints out the list, computes the maximum element of the list, and prints it out.
print('\nThe list is:', L)

min_element = 0
max_element = 99
for e in L:
    if e > min_element:
        min_element = e
    if e < max_element:
        max_element = e
print('\nThe maximum difference between largest and smallest values in this list is:',
      max_element - min_element
     )
print('Confirming with builtin operations:', max(L) - min(L))


#lab14

# lanb20


#################################################################################
# 2018S2-q7  寻找包含的字符



#2018 S2 -q8  字典的遍历  


#############################################################################
#2018S2-q5  读CSV文件
'''
Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''

import csv

def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    # Insert your code here
    years = list(range(1913,2014))
    max_value = None
    with open('cpiai.csv') as csvfile:
        for line in csvfile:
            if line.startswith("Date"):
                continue
            else:
                whole_date,index,inflation = line.split(',')
                year_num,mon_num,day_num = whole_date.split('-')
                if year_num ==str(year):
                    if max_value is None:
                        max_value = float(inflation)
                    else:
                        max_value = max(max_value,float(inflation))
    L = []
    with open('cpiai.csv') as csvfile:
        for line in csvfile:
            if line.startswith("Date"):
                continue
            else:
                whole_date,index,inflation = line.split(',')
                year_num,mon_num,day_num = whole_date.split('-')
                if year_num ==str(year) and float(inflation) >=max_value:
                    L.append(months[int(mon_num) - 1])
    print(f'In {year}, maximum inflation was: {max_value}')
    print(f'It was achieved in the following months: {", ".join(L)}')

if __name__ == '__main__':
    import doctest
    doctest.testmod()


#2018S2-q8   读txt文件


#2019 s1 Q4
from collections import defaultdict


def words(text):
    '''
    You can assume that "text" contains nothing but words that consist of nothing but letters
    (no apostrophe, no hyphen, no quote symbol...), possibly followed by commas, full stops,
    colons, semicolons, question marks and exclamation marks (all with no space before, and
    with a space after if not the last character).
    Prints out lists of words with all uppercase letters changed to lowercase,
    with no duplicate, in lexicographic order, grouped together by number of letters,
    from smallest number of letters to largest number of letters.
    Observe that each list of words is preceded with 4 spaces.

    >>> words('Twelve will, believe me, be quite enough for your purpose.')
    Words of length 2:
        ['be', 'me']
    Words of length 3:
        ['for']
    Words of length 4:
        ['will', 'your']
    Words of length 5:
        ['quite']
    Words of length 6:
        ['enough', 'twelve']
    Words of length 7:
        ['believe', 'purpose']
    >>> words('What was that? What does the Bishop mean?')
    Words of length 3:
        ['the', 'was']
    Words of length 4:
        ['does', 'mean', 'that', 'what']
    Words of length 6:
        ['bishop']
    >>> words('You must not fall into the common error of mistaking these simpletons '\
              'for liars and hypocrites. They believe honestly and sincerely that their '\
              'diabolical inspiration is divine. Therefore you must be on your guard against '\
              'your natural compassion. You are all, I hope, merciful men: how else could you '\
              'have devoted your lives to the service of our gentle Savior? You are going '\
              'to see before you a young girl, pious and chaste; for I must tell you, gentlemen, '\
              'that the things said of her by our English friends are supported by no evidence, '\
              'whilst there is abundant testimony that her excesses have been excesses of religion '\
              'and charity and not of worldliness and wantonness.')
    Words of length 1:
        ['a', 'i']
    Words of length 2:
        ['be', 'by', 'is', 'no', 'of', 'on', 'to']
    Words of length 3:
        ['all', 'and', 'are', 'for', 'her', 'how', 'men', 'not', 'our', 'see', 'the', 'you']
    Words of length 4:
        ['been', 'else', 'fall', 'girl', 'have', 'hope', 'into', 'must', 'said', 'tell', 'that', 'they', 'your']
    Words of length 5:
        ['could', 'error', 'going', 'guard', 'liars', 'lives', 'pious', 'their', 'there', 'these', 'young']
    Words of length 6:
        ['before', 'chaste', 'common', 'divine', 'gentle', 'savior', 'things', 'whilst']
    Words of length 7:
        ['against', 'believe', 'charity', 'devoted', 'english', 'friends', 'natural', 'service']
    Words of length 8:
        ['abundant', 'evidence', 'excesses', 'honestly', 'merciful', 'religion']
    Words of length 9:
        ['gentlemen', 'mistaking', 'sincerely', 'supported', 'testimony', 'therefore']
    Words of length 10:
        ['compassion', 'diabolical', 'hypocrites', 'simpletons', 'wantonness']
    Words of length 11:
        ['inspiration', 'worldliness']
    '''
    # print()
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    if text:
        lines = text.replace(",", "").replace(";", "").replace(".", "").replace("?", "").replace(":", "").split()

        words = defaultdict(set)
        for line in lines:
            words[len(line)].add(line.lower())

        keys = words.keys()
        for length in sorted(keys):
            print(f"Words of length {length}:")
            print(f"    {sorted(words[length])}")


if __name__ == '__main__':
    import doctest

    doctest.testmod()

#2019 s1 Q8
dictionary_file = 'dictionary.txt'


def number_of_words_in_dictionary(word_1, word_2):
    '''
    "dictionary.txt" is stored in the working directory.

    >>> number_of_words_in_dictionary('company', 'company')
    Could not find company in dictionary.
    >>> number_of_words_in_dictionary('company', 'comparison')
    Could not find at least one of company and comparison in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'comparison')
    Could not find at least one of COMPANY and comparison in dictionary.
    >>> number_of_words_in_dictionary('company', 'COMPARISON')
    Could not find at least one of company and COMPARISON in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'COMPANY')
    COMPANY is in dictionary.
    >>> number_of_words_in_dictionary('COMPARISON', 'COMPARISON')
    COMPARISON is in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'COMPARISON')
    Found 14 words between COMPANY and COMPARISON in dictionary.
    >>> number_of_words_in_dictionary('COMPARISON', 'COMPANY')
    Found 14 words between COMPARISON and COMPANY in dictionary.
    >>> number_of_words_in_dictionary('CONSCIOUS', 'CONSCIOUSLY')
    Found 2 words between CONSCIOUS and CONSCIOUSLY in dictionary.
    >>> number_of_words_in_dictionary('CONSCIOUS', 'CONSCIENTIOUS')
    Found 3 words between CONSCIOUS and CONSCIENTIOUS in dictionary.
    '''
    # print()
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    with open(dictionary_file) as file:
        lines = [line.strip() for line in file.readlines()]

        if word_1 == word_2:
            if word_1 in lines:
                print(f"{word_1} is in dictionary.")
            else:
                print(f"Could not find {word_1} in dictionary.")
        else:
            if word_1 in lines and word_2 in lines:
                start = lines.index(word_1)
                end = lines.index(word_2)
                print(f"Found {abs(start - end) + 1} words between {word_1} and {word_2} in dictionary.")
            else:
                print(f"Could not find at least one of {word_1} and {word_2} in dictionary.")


if __name__ == '__main__':
    import doctest

    doctest.testmod()


################################################################################
#打印

2019 s1  6
def rectangle(width, height):
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when z is reached.

    >>> rectangle(1, 1)
    a
    >>> rectangle(2, 3)
    ab
    dc
    ef
    >>> rectangle(3, 2)
    abc
    fed
    >>> rectangle(17, 4)
    abcdefghijklmnopq
    hgfedcbazyxwvutsr
    ijklmnopqrstuvwxy
    ponmlkjihgfedcbaz
    '''
    # print()
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    # 1.两种,边打印，边输出 2.放到list 一起打印
    start = ord('a')
    total = 0
    for height_index in range(height):
        line = ""
        for width_index in range(width):
            line += chr(start + total % 26)
            total += 1
        if height_index % 2 == 0:
            print(line)
        else:
            print(line[::-1])


if __name__ == '__main__':
    import doctest

    doctest.testmod()
'''
#Decodes all multiplications of the form

                       *  *  *
                  x       *  *
                    ----------
                    *  *  *  *
                    *  *  *
                    ----------
                    *  *  *  *

#such that the sum of all digits in all 4 columns is constant.
#Decoding一个乘法
#We想要解码表单的所有乘法
#such，所有4列中所有数字的总和是不变的。
'''
for i in range(100,1000):  #取第一个三位数，遍历 100 到1000之间
    for j in range(10,100): #取第一个二位数，遍历 10 到100之间
        first_outcome = i * (j % 10) #进行乘法，j的个位乘以i
        if not 1000 <= first_outcome <=9999:
            continue  # 会直接跳出这个循环返回小循环继续执行
        second_outcome = i *(j // 10) #进行乘法，j的十位乘以i
        if not 100 <= second_outcome <999:
            continue
        final_outcome = first_outcome + 10 * second_outcome #得出最终的结果
        if not 1000 <= final_outcome <= 9999: #判断是否为4位数
            continue
        #因为在题目中要求四列加起来的值要相等
        sum_col1 = int(str(i)[-1]) + int(str(j)[-1])\
                    + int(str(first_outcome)[-1]) + int(str(final_outcome)[-1])
        sum_col2 = int(str(i)[-2]) + int(str(j)[-2])\
                    + int(str(first_outcome)[-2]) + int(str(second_outcome)[-1])\
                    + int(str(final_outcome)[-2])
        sum_col3 = int(str(i)[-3]) + int(str(first_outcome)[-3]) + int(str(second_outcome)[-2])\
                    + int(str(final_outcome)[-3])
        sum_col4 = int(str(first_outcome)[0]) + int(str(second_outcome)[0])\
                    + int(str(final_outcome)[0])
        if sum_col1 == sum_col2 == sum_col3 == sum_col4:
            print(f"{i}*{j} = {final_outcome},all columns adding to {sum_col1}.")


# 2018S2-q7  自上而下打印    (从上到下打印0，1，2，3)
def f(height):
    '''
    >>> f(1)
    0
    >>> f(2)
     0
    123
    >>> f(3)
      0
     123
    45678
    >>> f(4)
       0
      123
     45678
    9012345
    >>> f(5)
        0
       123
      45678
     9012345
    678901234
    >>> f(6)
         0
        123
       45678
      9012345
     678901234
    56789012345
    >>> f(20)
                       0
                      123
                     45678
                    9012345
                   678901234
                  56789012345
                 6789012345678
                901234567890123
               45678901234567890
              1234567890123456789
             012345678901234567890
            12345678901234567890123
           4567890123456789012345678
          901234567890123456789012345
         67890123456789012345678901234
        5678901234567890123456789012345
       678901234567890123456789012345678
      90123456789012345678901234567890123
     4567890123456789012345678901234567890
    123456789012345678901234567890123456789
    '''

def f(height):
    count = 0
    for i in range(height):  # 打印空格
        print(" " * (height - i - 1), end='')  #打印空格 print默认是打印一行，结尾加换行。end=' '意思是末尾不换行，加空格。

        for j in range(2 * i + 1):  # j 代表打印几个数字出来  通过 (2 * i + 1)得出
            print(count % 10, end='')  # count % 10 取余数 保证了，尽管count会变得越来越大，但是打印出来的永远是个位数 0~9
            count += 1   #count 真正决定了打印的是 哪个数字 
        print()


if __name__ == '__main__':
    import doctest
    doctest.testmod()


#2019 final 打印原题
## 2017 S1-q7  自上而下打印  打印输出字符

''' ord(c) returns the encoding of character c.
    chr(e) returns the character encoded by e.
'''


def f(n):
    '''
    >>> f(1)
    A
    >>> f(2)
     A
    CBC
    >>> f(3)
      A
     CBC
    EDCDE
    >>> f(4)
       A
      CBC
     EDCDE
    GFEDEFG
    >>> f(30)
                                 A
                                CBC
                               EDCDE
                              GFEDEFG
                             IHGFEFGHI
                            KJIHGFGHIJK
                           MLKJIHGHIJKLM
                          ONMLKJIHIJKLMNO
                         QPONMLKJIJKLMNOPQ
                        SRQPONMLKJKLMNOPQRS
                       UTSRQPONMLKLMNOPQRSTU
                      WVUTSRQPONMLMNOPQRSTUVW
                     YXWVUTSRQPONMNOPQRSTUVWXY
                    AZYXWVUTSRQPONOPQRSTUVWXYZA
                   CBAZYXWVUTSRQPOPQRSTUVWXYZABC
                  EDCBAZYXWVUTSRQPQRSTUVWXYZABCDE
                 GFEDCBAZYXWVUTSRQRSTUVWXYZABCDEFG
                IHGFEDCBAZYXWVUTSRSTUVWXYZABCDEFGHI
               KJIHGFEDCBAZYXWVUTSTUVWXYZABCDEFGHIJK
              MLKJIHGFEDCBAZYXWVUTUVWXYZABCDEFGHIJKLM
             ONMLKJIHGFEDCBAZYXWVUVWXYZABCDEFGHIJKLMNO
            QPONMLKJIHGFEDCBAZYXWVWXYZABCDEFGHIJKLMNOPQ
           SRQPONMLKJIHGFEDCBAZYXWXYZABCDEFGHIJKLMNOPQRS
          UTSRQPONMLKJIHGFEDCBAZYXYZABCDEFGHIJKLMNOPQRSTU
         WVUTSRQPONMLKJIHGFEDCBAZYZABCDEFGHIJKLMNOPQRSTUVW
        YXWVUTSRQPONMLKJIHGFEDCBAZABCDEFGHIJKLMNOPQRSTUVWXY
       AZYXWVUTSRQPONMLKJIHGFEDCBABCDEFGHIJKLMNOPQRSTUVWXYZA
      CBAZYXWVUTSRQPONMLKJIHGFEDCBCDEFGHIJKLMNOPQRSTUVWXYZABC
     EDCBAZYXWVUTSRQPONMLKJIHGFEDCDEFGHIJKLMNOPQRSTUVWXYZABCDE
    GFEDCBAZYXWVUTSRQPONMLKJIHGFEDEFGHIJKLMNOPQRSTUVWXYZABCDEFG

    >>> f(3)
      A
     CBC
    EDCDE
    '''
    lines = []
    for i in range(n):  # 决定行数
        start = ord('A') + i % 26  # 起始位置
        line = []
        for j in range(1,i + 1):  #两层  for 循环 
            line.append(chr(ord('A') + (i + j) % 26))
        new_line = []
        if line:
            new_line.extend([' '] * (n - i-1))
            new_line.extend(reversed(line))
            new_line.append(chr(start))  # 拼接四三部分 空格，reversed(line)，start，line
            new_line.extend(line)
        else:
            new_line.extend([' '] * (n - i-1))
            new_line.append(chr(start))
        lines.append("".join(new_line))
    for line in lines:
        # output_line = line.ljust(n,' ')
        print(f'{line}')


if __name__ == '__main__':
    import doctest
    doctest.testmod()


# lab11 自上而下打印
'''
Prompts the user for a strictly positive number N
and outputs an equilateral triangle of height N.
The top of the triangle (line 1) is labeled with the letter A.
For all nonzero p < N, line p+1 of the triangle is labeled
with letters that go up in alphabetical order modulo 26
from the beginning of the line to the middle of the line,
starting with the letter that comes next in alphabetical order
modulo 26 to the letter in the middle of line p,
and then down in alphabetical order modulo 26
from the middle of the line to the end of the line.
提示用户严格正数N.
并输出高度为N的等边三角形。
三角形的顶部（第1行）标有字母A.
对于所有非零p <N，标记三角形的线p + 1
用字母顺序上升的字母26
从行的开头到行的中间，
从字母顺序下一个字母开始
模数26到p行中间的字母，
然后按字母顺序向下模26
从线的中间到线的末端。


    A
   BCB
  DEFED
 GHIJIHG
KLMNONMLK
'''
# 仿照这种写法来

while True:
    try:
        height = int(input('Enter strictly positive number'))
        if height <= 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect input, try again.')

triange = []  #三角形
last_char = ord('A')
for i in range(height):
    temp_list1 = []  # 初始化一个空的list
    temp_list2 = []
    for j in range(i+1):
        if last_char == ord('Z') + 1: #这里的意思是，如果到Z之后，Z的下一位
            last_char = ord('A')     #变成A
        temp_list1.append(last_char)
        last_char += 1 #依次+1
    temp_list2 = list(temp_list1) #复制一份给list2
    temp_list2.reverse()
    temp_list2 = temp_list2[1:] #不要temp_list2 的第一位
    triange.append((temp_list1 + temp_list2)) #拼接到一起
count = 1
for i in range(len(triange)):
    print(' '*(height - i - 1), end='') # 这里是如何打印字母前的空格
    for e in triange[i]:        #end=''换行
        print(f'{chr(e)}',end ='')
    print()


#lab12  杨辉三角
'''
Prompts the user for a number N and prints out the first N + 1 lines of Pascal triangle.
Write a program pascal_triangle.py that prompts the user for a number N and prints out the 
first N + 1 lines of Pascal triangle, making sure the numbers are nicely aligned, as illustrated for N = 3, 7 and 11:
   1
  1 1
 1 2 1
1 3 3 1


        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
  1 5 10 10 5 1
 1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
'''


while True:
    try:
        N = int(input('Enter a nonnegative integer: '))
        if N < 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect input, try again')
pascal_triangle = [[1] * (n + 1) for n in range(N + 1)]
for n in range(2, N + 1):
    for k in range(1, n // 2 + 1):
        pascal_triangle[n][k] = pascal_triangle[n - 1][k - 1] + pascal_triangle[n - 1][k]
    for k in range(1, (n + 1) // 2):
        pascal_triangle[n][n - k] = pascal_triangle[n][k]
width = len(str(pascal_triangle[N][N // 2]))
for n in range(N + 1):
    print(' ' * width * (N - n), end = '')
    print((' ' * width).join((f'{pascal_triangle[n][k]:{width}d}' for k in range(n + 1))))




# 2018S1-q7  自下而上打印
def f(height):
    '''
    >>> f(1)
    0
    >>> f(2)
    101
     0
    >>> f(3)
    21012
     101
      0
    >>> f(5)
    432101234
     3210123
      21012
       101
        0
    >>> f(10)
    9876543210123456789
     87654321012345678
      765432101234567
       6543210123456
        54321012345
         432101234
          3210123
           21012
            101
             0
    >>> f(15)
    43210987654321012345678901234
     321098765432101234567890123
      2109876543210123456789012
       10987654321012345678901
        098765432101234567890
         9876543210123456789
          87654321012345678
           765432101234567
            6543210123456
             54321012345
              432101234
               3210123
                21012
                 101
                  0
    >>> f(26)
    543210987654321098765432101234567890123456789012345
     4321098765432109876543210123456789012345678901234
      32109876543210987654321012345678901234567890123
       210987654321098765432101234567890123456789012
        1098765432109876543210123456789012345678901
         09876543210987654321012345678901234567890
          987654321098765432101234567890123456789
           8765432109876543210123456789012345678
            76543210987654321012345678901234567
             654321098765432101234567890123456
              5432109876543210123456789012345
               43210987654321012345678901234
                321098765432101234567890123
                 2109876543210123456789012
                  10987654321012345678901
                   098765432101234567890
                    9876543210123456789
                     87654321012345678
                      765432101234567
                       6543210123456
                        54321012345
                         432101234
                          3210123
                           21012
                            101
                             0
    '''
    # Insert your code here
def f(height):
    n = height
    while n > 0:
        values = [str(i % 10) for i in range(n)]
        #打印的时候进行拼接就可以了
        print (" " * (height - n) + "".join(reversed(values[1:])) + "".join(values))
        n -=1
if __name__ == '__main__':
    import doctest
    doctest.testmod()


'''
    >>> f(1)
    0
    >>> f(2)
    123
     0
    >>> f(3)
    45678
     123
      0
    >>> f(5)
    678901234
     9012345
      45678
       123
        0
'''

def f(height):
    count = 0
    lines=[]
    value = []
    n = height
    while n > 0:
        for i in range(height):  # 打印空格
              # 打印空格 print默认是打印一行，结尾加换行。end=' '意思是末尾不换行，加空格。
            for j in range(2 * i + 1):  # j 代表打印几个数字出来  通过 (2 * i + 1)得出
                value = [" " * (height - i - 1) + count % 10]  # count % 10 取余数 保证了，尽管count会变得越来越大，但是打印出来的永远是个位数 0~9
                count += 1  # count 真正决定了打印的是 哪个数字
                lines.append("".join(value))
                n -= 1
        for line in reversed(lines):
            print(f'{line}')
#############################################################################################
字典操作

2018 s2  final  2
def f(N):
    '''
    >>> f(20)
    Here are your banknotes:
    $20: 1
    >>> f(40)
    Here are your banknotes:
    $20: 2
    >>> f(42)
    Here are your banknotes:
    $2: 1
    $20: 2
    >>> f(43)
    Here are your banknotes:
    $1: 1
    $2: 1
    $20: 2
    >>> f(45)
    Here are your banknotes:
    $5: 1
    $20: 2
    >>> f(2537)
    Here are your banknotes:
    $2: 1
    $5: 1
    $10: 1
    $20: 1
    $100: 25
    '''
    banknote_values = [1, 2, 5, 10, 20, 50, 100]
    banknotes = dict.fromkeys(banknote_values, 0)
    # 用 fromkeys 来创建字典 生成这样的形式 {1:0，2:0, 5:0，10:0, 20:0, 50:0，100:0}
    index = len(banknote_values) - 1  # index = 6
    while N > 0 and index >= 0:
        count, N = divmod(N, banknote_values[index]) # 从 index=6  也就是100 开始
        if count > 0:
            banknotes[banknote_values[index]] = count #对字典进行更新
        index -= 1

    print('Here are your banknotes:')
    for value in sorted(banknotes):
        if banknotes[value]:
            print('${}: {}'.format(value, banknotes[value]))


if __name__ == '__main__':
    import doctest

    doctest.testmod()











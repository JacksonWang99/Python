import sys
from random import seed, randint, randrange


try:
    arg_for_seed, upper_bound, length =\
            (int(x) for x in input('Enter three integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
def length_of_longest_increasing_sequence(L):
    if len(L)==0:
        return 0
    if len(L)==1:
    	return 1
    l=[]                        定义一个空数列            
    l.extend(L)                 原数列
    Line1=L                     生成Line1
    Line1.extend(L)             用extend() 函数把原数列double 一下
    Line2=[]                    
    Line3=[Line1 [0]]           Line3 是存储符合递增数列的集合，Line3里已经存在Line1的第0 位
    for i in range(len(Line1)-1):             这一步是用来生成指针（位置值，len(Line1)-1 的原因是防止溢出）
        if Line1[i]<= Line1[i+1]:             当Line1 第i 位的数字 大于 第i+1 位的数字时，
            Line3.append(Line1[i+1])          把新找到的 Line1[i+1]  加到 Line3 里面
        else:
        	if len(Line2) < len(Line3):
        		Line2=Line3                   在这里由于Line3没经过一次上面的if 循环，如果满足条件Line3 
                                              就会增加一个新的数，正好把Line3赋值给Line2,也就是说Line2 是在不断的变长 
        	Line3 = [Line1[i+1]]              这里把Line 3 清空，Line3里面还剩上次结束时的最后一位，用来进行下次比较操作   

    if len(Line2) < len(Line3):
        		Line2=Line3

    if len(Line2) > len(l):                   如果新生成的数列 Line2的长度大于原来的数列 l，那么就直接输出
        return len(l)                         原来数列的长度，这种情况只应用与数列内部元素全部相等的情况。
    else:
        return len(Line2)                     如果不是，就输出Line2 的长度。


def max_int_jumping_in(L):
    if len(L) == 0:
        return 0
    a = b = c = 0 
    Line4 = []
    Line5 = ''
    for a in range(len(L)):
        b = a
        while b not in Line4:
            Line4.append(b)
            Line5 += str(L[b])
            b = L[b]
        else:
            if Line5 != '':
                c = max(c, int(Line5))
            Line5 , Line4 = '', []
    return c


seed(arg_for_seed)
L_1 = [randint(0, upper_bound) for _ in range(length)]
print('L_1 is:', L_1)
print('The length of the longest increasing sequence\n'
      '  of members of L_1, possibly wrapping around, is:',
      length_of_longest_increasing_sequence(L_1), end = '.\n\n'
     )
L_2 = [randrange(length) for _ in range(length)]
print('L_2 is:', L_2)
print('The maximum integer built from L_2 by jumping\n'
      '  as directed by its members, from some starting member\n'
      '  and not using any member more than once, is:',
      max_int_jumping_in(L_2)
     )


















#多种答案
def max_int_jumping_in(L):
    if len(L) == 0:
        return 0
    a1=0
    L4=[]
    L5=[]
    for i in range(len(L)):
        while i not in L4:
            L4.append(i)
            a1=str(L[i])
            Line5 += str(L[i])
            i=L(i)
        if Line5 != '':
                a1 = max(a1, int(Line5))
            Line5 , L4 = '', []
    return

def max_int_jumping_in(L):
    if len(L) == 0:
        return 0
    a1=a2=a3=a4=''
    l=[]
    L4=[]
    L5=[]
    for i in range(len(L)):
        l.append(i)
        while i not in L4:
            L4.append(i)
            a1=str(L[i])
            a3+=a1
            L4.append(int(a1))
            a2=str(L[int(a1)])
            a3+=a2
            L4.append(int(a2))
            i=int(a2) 
		if 	
        L5.append(a3)
    a4=int(max(L5))
    return a4

#正确
def max_int_jumping_in(L):
    if len(L) == 0:
        return 0
    a = b = c = 0 
    Line4 = []
    Line5 = ''
    for a in range(len(L)):
        b = a
        while b not in Line4:
            Line4.append(b)
            Line5 += str(L[b])
            b = L[b]
        else:
            if Line5 != '':
                c = max(c, int(Line5))
            Line5 , Line4 = '', []
    return c

#正确
def max_int_jumping_in(L):
  if len(L) == 0:
        return 0
    b = c = 0 
    Line4 = []
    Line5 = ''
    for i in range(len(L)):
        b = i
        while b not in Line4:
            Line4.append(b)
            Line5 += str(L[b])
            b = L[b]
        else:
            if Line5 != '':
                c = max(c, int(Line5))
            Line5 , Line4 = '', []
    return c

#正确
def max_int_jumping_in(L):
  if len(L) == 0:
        return 0
    k = j = 0 
    Line4 = []
    Line5 = ''
    for i in range(len(L)):
        k = i
        while k not in Line4:
            Line4.append(k)
            Line5 += str(L[k])
            k = L[k]
        else:
            if Line5 != '':
                j = max(j, int(Line5))
            Line5 , Line4 = '', []
    return j


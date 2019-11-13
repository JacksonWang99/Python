# Written by Eric Martin for COMP9021
# 托雷斯祝您VAN♂事如意
# 抄袭有风险，学到才是自己的

import sys
from random import seed, randint, randrange


try:
    arg_for_seed, upper_bound, length =\
            (int(x) for x in input('Enter three integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()



def length_of_longest_increasing_sequence(L):
    if len(L) == 0:
        return 0
    LL = L
    LL.extend(L)
    a = b  = n = 0
    for i in LL:
        if i >= n:
            a += 1
        else:
            b = max(a,b)
            a = 1
        n = i
    if max(a,b) > len(L):
        return False
    else:
        return max(a,b)


	

def max_int_jumping_in(L):
    if len(L) == 0:
        return 0
    l = []
    for i in range(len(L)):
        l.append(i)

    a = b = maxx = 0 
    ll = []
    maxz = ''
    for a in range(len(L)):
        b = a
        while b not in ll:
            ll.append(b)
            maxz += str(L[b])
            b = L[b]
        if maxz != '':
            maxx = max(maxx, int(maxz))
        maxz , ll = '', []
    return maxx

        

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




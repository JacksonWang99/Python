# Prompts the user for a positive integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived positive integer that codes the set of running sums
# ot the members of S when those are listed in increasing order.
#
'''杰克买买提祝您圆满成功'''


from itertools import accumulate
import sys

try:
    n = int(input('Input a positive integer: '))
    if n < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

# POSSIBLY DEFINE OTHER FUNCTIONS# 杰克买买提祝您圆满成功
def display_n(n):
    if n == 0:
        print('{}')
    else:
        l = [1 for n in range(n+1)]
        l[0] = 0
        for i in range(1,n+1):
            if i%2 == 0:
                l[i] = l[i]*i/2
            else:
                l[i] = l[i]*((i//2)+1)*(-1)
        b = bin(n)[2:]
        b = b[::-1]
        s = []
        for i in range(len(b)):
            if b[i] == "1":
                s.append(l[i])
        s = sorted(s)
        for i in range(len(s)):
            s[i] = int(s[i])

        string = '{'
        for i in range(len(s)-1):
            string = string + str(s[i]) + ', '
        string = string + str(s[-1]) + '}'
        print(string)

    # REPLACE pass ABOVE WITH CODE TO PRINT OUT ENCODED SET (WITH print() STATEMENTS)
    # 杰克买买提祝您圆满成功
def code_derived_set(n):
    if n == 0 :
        return 0
    else:
        encoded_running_sum = 0
        # 杰克买买提祝您圆满成功

        if n == 0:
            print('{}')
        else:
            l = [1 for n in range(n+1)]
            l[0] = 0

            for i in range(1,n+1):
                if i%2 == 0:
                    l[i] = l[i]*i/2
                else:
                    l[i] = l[i]*((i//2)+1)*(-1)
            b = bin(n)[2:]
            b = b[::-1]
            s = []
            for i in range(len(b)):
                if b[i] == "1":
                    s.append(l[i])
            s = sorted(s)
            for i in range(len(s)):
                s[i] = int(s[i])
                # 杰克买买提祝您圆满成功

        for i in range(len(l)):
                l[i] = int(l[i])
        derived_list = []
        for i in range(1,len(s)+1):
            derived_list.append(sum(s[0:i]))
        derived_list = sorted(derived_list)
        #print('Q2 output derived_list=',derived_list) #这里输出Q2答案
        #Q2 solution

        # reverse derived list
        #derived_list = derived_list[::-1]

        #print('derived_list=',derived_list)
        max_index = -1
        for i in range(len(derived_list)):
            if l.index(derived_list[i]) > max_index:
                max_index = l.index(derived_list[i])
        #print('max_index=',max_index)

        l = l[:max_index+1]
        #print('slice l to =',l)
        # 现在再用截取好的 l 去和 derived_list去比较,操作出 binary_string
        bin_list = [0 for i in range(len(l))]
        #print('bin_list  = ',bin_list)
        for i in range(len(l)):
            if l[i] in derived_list:
                bin_list[i] = 1
        #print('bin_listafter=',bin_list)
        bin_list = bin_list[::-1]
    #print('bin_listafter=',bin_list)

        bin_str = ''.join(str(e) for e in bin_list)
    #print('Q3 solution',int(bin_str,2))

        encoded_running_sum = int(bin_str,2)
        return encoded_running_sum

print('The encoded set is: ', end = '')
display_n(n)
encoded_running_sum = code_derived_set(n)
print('The derived encoded set is: ', end = '')
display_n(encoded_running_sum) # print
print('  It is encoded by:', encoded_running_sum)
# 杰克买买提祝您圆满成功

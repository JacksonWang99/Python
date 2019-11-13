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
# Written by *** and Eric Martin for COMP9021


from itertools import accumulate
import sys

try:
    encoded_set = int(input('Input a positive integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


# POSSIBLY DEFINE OTHER FUNCTIONS
def encode(n):  # encoded_set 编码集,这里是创建一个 encode函数，进行转化
    if n % 2 == 0:
        w = int(n / 2)
        return w
    else:
        w = int(-((n + 1) / 2))
        return w


def display_encoded_set(encoded_set):  # 显示编码集
    L = bin(encoded_set)[2:][::-1]
    # if encoded_set == 0:
    #     return
    # else:
    W = []
        # i 为二进制的第几位
    for i in range(len(L)):
        if L[i] == '1':
                # 如果二进制的对应位置是1 ，我们就加他对应位置encode 的结果
            W.append(encode(i))
    return sorted(W)  #排序

def exchange_encode1(n):  #对数列进行反向转变
    if n >= 0:
        m = n * 2
        return m
    else:
        m = -(n * 2 + 1)
        return m


def code_derived_set(encoded_set):
    if encoded_set == 0:
        print('The derived encoded set is:' + ' {}')
        return 0
    else:
        LL = set()
        for i in accumulate(display_encoded_set(encoded_set)):
            LL.add(i)  #迭代求数列，生成LL

        print('The derived encoded set is:'+' {'+
              (str(sorted(list(LL)))).replace('[','').replace(']','')+'}')
        L = []
        for i in LL:
            L.append(exchange_encode1(i))
        Binary_list = ['0' for i in range(max(L) + 1)]
        for i in L:
            Binary_list[i] = '1'
        Binary_list.reverse()
        Binary_list = ''.join(Binary_list)
        encoded_running_sum = int(Binary_list, 2)
        return encoded_running_sum   #返回最终的和

# print(encoded_running_sum)

print('The encoded set is: ', end = '')  # 编码集
print('{'+(str(display_encoded_set(encoded_set))).replace('[','').replace(']','')+'}')
encoded_running_sum = code_derived_set(encoded_set)
# display_encoded_set(encoded_running_sum)
print('  It is encoded by:', encoded_running_sum)
    
from itertools import accumulate
import sys

try:
    encoded_set = int(input('Input a positive integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


# POSSIBLY DEFINE OTHER FUNCTIONS
def encode(n):  # encoded_set 编码集,这里是创建一个 encode函数
    if n % 2 == 0:
        w = int(n / 2)
        return w
    else:
        w = int(-((n + 1) / 2))
        return w


def display_encoded_set(encoded_set):  # 显示编码集

    L = bin(encoded_set)[2:][::-1]
    if encoded_set == 0:
        print('{}')
    else:
        W = []
        # i 为二进制的第几位
        for i in range(len(L)):
            if L[i] == '1':
                # 如果二进制的对应位置是1 ，我们就加他对应位置encode 的结果
                W.append(encode(i))
                W = sorted(W)
        string = '{'
        for e in range(len(W) - 1):
            string = string + str(W[e]) + ', '
        string = string + str(W[-1]) + '}'


#print(string)    # 错误，这里不能是print，print是直接打印出来，在屏幕上显示
# 但是quiz最后有专门的打印，不需要进行额外的Print,这里的 return 的作用是暂时存储
#因为生成的序列要被下一个函数调用，以及最后的打印调用，所以要返回值，其次对于
#def函数来说，肯定是要有返回值的，因为调用函数就是调用函数生成的值和内容


def exchange_encode1(n):
    if n >= 0:
        m = n * 2
        return m
    else:
        m = -(n * 2 + 1)
        return m


def code_derived_set(encoded_set):
    LL = set()
    for i in sorted(list(accumulate(sorted(display_encoded_set(encoded_set))))):
        LL.add(i)
    L = []
    for i in LL:
        L.append(exchange_encode1(i))
    Binary_list = ['0' for i in range(max(L) + 1)]
    for i in L:
        Binary_list[i] = '1'
    Binary_list.reverse()
    Binary_list = ''.join(Binary_list)
    encoded_running_sum = int(Binary_list, 2)


print(encoded_running_sum)

print('The encoded set is: ', end = '')  # 编码集
display_encoded_set(encoded_set)
encoded_running_sum = code_derived_set(encoded_set)
print('The derived encoded set is: ', end = '')
display_encoded_set(encoded_running_sum)
print('  It is encoded by:', encoded_running_sum)
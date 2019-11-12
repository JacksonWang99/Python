# Written by Eric Martin for COMP9021
#
# Prompts the user for an arity (a natural number) n and a word.
#提示用户输入一个参数数量(一个自然数)n和一个单词。
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores. 将符号称为只由字母字符和下划线组成的单词
# Checks that the word is valid, in that it satisfies the following
# inductive definition: 检查单词是否有效，因为它满足以下归纳定义
# - a symbol, with spaces allowed at both ends, is a valid word;
    #符号的两端允许有空格，它是一个有效的单词
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends
#   and around parentheses and commas, is a valid word.
    #一个单词的形式例如s(w_1，…，w_n)，其中s表示符号，w_1，…， w_n表示有效单词，
    # 在两端和圆括号和逗号周围允许有空格，这是一个有效单词


import sys


def is_valid(word, arity):
    Valid_invalid = False
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
    # 1. check 是否有s，若果有s, 是不是一个完整的s,完整的两个括号。
    # 如果没有s，那就是单独的一个字母arity判断数量。
    # 如果没有s，那就是单独的一个字母arity判断数量。
    # 2如果有S 那么这个s里面的参数数量，是否等于arity，
    # 3 如果s中 某个参数仍然是一个s的形式,依然要判断这个子s 是否满足上述的条件
    word_str = word.replace(' ', '')
    valid_chars = ['_', '(', ')', ',']
    invalid_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for item in word_str:
        if item.isalpha():
            continue
        elif item in valid_chars:
            continue
        elif item in invalid_chars:
            return False
        else:
            return False

    if word_str.count('(') != word_str.count(')'):
        return False
    if word_str.count('(') == 0 and word_str.count(')') == 0 and arity == 0:
        return True
    if word_str.count('(') == 0 and word_str.count(')') == 0 and arity != 0:
        return False


    if word_str:
        while word_str.find(')') > 0:

            # f(a, FF(a, b, fff(a, b, c, FfFf(a,b,c,d)), FfFf(a,b,c,d)), c,d)
            #从右往左读
            First_index = word_str.rindex('(')

            left_str = word_str[0:First_index]

            second_index = word_str[First_index:].index(')') + First_index

            right_str = word_str[second_index + 1:]

            mid_list = word_str[First_index + 1: second_index] #取的时候不取括号，直接取括号里面的变量值，省略括号
            ''' 从左往右读
            First_index = word_str.index(')')
            right_str = word_str[First_index + 1:]
            second_index = word_str[0:First_index].rindex('(')
            left_str = word_str[0:second_index]
            mid_list = word_str[second_index + 1: First_index]'''

            The_arity_list = mid_list.split(',')

            M = len(The_arity_list)
            if M == arity:
                word_str = left_str + right_str
            else:
                Valid_invalid = False
                break
        else:
            Valid_invalid = True
    return Valid_invalid

'''def is_valid(word, arity):
    Valid_invalid = False
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
    # 1. check 是否有s，若果有s, 是不是一个完整的s,完整的两个括号。
    # 如果没有s，那就是单独的一个字母arity判断数量。
    # 如果没有s，那就是单独的一个字母arity判断数量。
    # 2如果有S 那么这个s里面的参数数量，是否等于arity，
    # 3 如果s中 某个参数仍然是一个s的形式,依然要判断这个子s 是否满足上述的条件

    word_str = word.replace(' ', '')
    valid_chars = ['_', '(', ')', ',']
    for item in word_str:
        if item.isalpha() or item in valid_chars:
            continue
        else:
            return False
    if word_str.count('(') != word_str.count(')'):
        return False
    if word_str.count('(') == 0 and word_str.count(')') == 0 and arity == 0:
        return True
    if word_str.count('(') == 0 and word_str.count(')') == 0 and arity != 0:
        return False
    
    if word_str:
        while word_str.find(')') > 0:
            #f(a, FF(a, b, fff(a, b, c, FfFf(a,b,c,d)), FfFf(a,b,c,d)), c,d)
            
            First_index = word_str.index(')')
            right_str = word_str[First_index + 1:]
            second_index = word_str[0:First_index].rindex('(')
            left_str = word_str[0:second_index]
            mid_list = word_str[second_index + 1: First_index]
            
            if len(mid_list.split(',')) == arity:
                word_str = left_str + right_str
            #最后剩下 f
            else:
                return False
                break
        else:
            Valid_invalid = True
    return Valid_invalid'''

try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()

word = input('Input a word: ')
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')


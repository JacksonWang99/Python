from collections import OrderedDict

ARABIC_TO_ROMAN = OrderedDict([
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
])


# 1.如果出现了相连续的数字
#   a.不可能出现4个连续     IIII
#   b.如果是升序，不可能出现两个连续的   I 1 X 10   IIX  VIII
#   c.如果出现2个连续的，这两个连续的一定是10幂次方 10**0  10**1
#   d.DED 肯定是19 或者是19的 10**n的数字 19*10**n
# 如果从右向左开始计算，第一个和第三个相等，那么E是1*10**n D是1 * 10**（n+1）
#   e.ABCA 罗马数字表示的最小数字49 或者是49的 10**n的数字 49*10**n
#   190   CXC
#
#
#
# 2. (1 I  4 IV    9 IX,  49 XLIX)
# D 50 C 10 B 5 A 1     1 A    4 AB  9 AC    49 CDAC

# 1 5
# 10 50
# 100 500
# 1000 5000
# 10000 50000
#
# 1*10**0     1*10**1      1*10**2
# 1         5 10        50 100          500  1000
# I         V X         L  C            D    M
#
# 降序表示累加，升序表示累减
# 1     I
# 2     II
# 3     III
# 4     IV 1 5   5-1 4
# 5     V
# 6     VI 5 1    6
# 7     VII 5 1 1 7
# 8     VIII 5 1 1 1 8
# 9     IX   1 10   9
# 49    XLIX (40 + 9)
#        X=10 L=50 I =1 X 10
#       XL = 40 IX = 9      49

# Please convert *** using DCBA
# 1000      500      100       50      10          5         1
# M         D        C           L      X         V        I
# 50      10     5       1
# D     C    B       A

# Please convert *** using ABCD
#
# A(50)     B(10) C(5)  D(1)

# Please convert *** using CA

# C(5)  A(1)

# Please convert *** using ***
# Please convert III using XVI
# X(10)   V(5) I (1)
# 3   III(3)   3 VVV
# # Please convert CDAC using DCBA
# D 50 C 10 B 5 A 1

# 10 50 1 10 = 40 + 9 = 49
# 49 <==> CDAC

#

# AC
# 1.C(1) A 5
# 2.AC 6


# using CA(C(5) A1
# C(5) A(1)
# AC 4


# ABCCDED
#
# D = 1   E 5
# DED   19
# DED   E (1) D(10)
#
# ABCC              DED
# A(1000)     B(500)    C (100)  D(10)   E(1)

# ABCCDED 1000 + 500 + 200 + 19 1719
# using         ABC_D_E

# 从右向左查找
# ABCADDEFGF
# FGF 第一个和第三个相等，F = 10,G = 1
# FGF = 19
# 490/4900
# 49 abca  c 1* 10**n  c = 1000
# ABCAFDDE ABCA A B(50000) A(10000) C(1000)  D 100 E = 50,F = 10（少了一个5） G =1
# 49000 + 200 + 50 + 19   49269

#               BA_C_DEF_G


# DCBA
# D(50)   C(10)  B(5)  A(1)


# 50: D
# 40: CD
# 10：C
# 9: AC
# 5:B
# 4:AB
# 1:A


# CAC

# 罗马数字转阿拉伯数字
# 1.做法从右向左，一位（最多两位）读取
# C             AC
#  10 +                     AC->9
# BAAA    B  A 1 A 1 A 1


# 49
# 49 >= 50
# 49 >= 40
# 9  >= 10
# 9 >=9 0

# 19
# 19>= 50
# 19>=40
# 19>=10  9
# 9>=9  AC

# CAC

# CAC

# 1.给定一个字符串（ABCD,DCBA,LXVI)
# 2.从右向左读取，标记每个字符的Value
# # I 1 V 5 X 10 L 50 C 100
# # A 1 B 5 C 10 D 50
# # D 1 C 5 B 10 A 50
# 第三步：创建字典
# I  1
# IV 4
# V  5
# IX 9
# X  10
# XL 40
# L  50
# XC 90

# 1 I
# 4 IV
# 5 V


# 第四步，根据创建的字典，去计算对应的数字转换
#


class InvalidProvidedValue(Exception):
    pass


# 第一问
def arabic_to_roman(initial_arabic_number):
    if initial_arabic_number < 1:
        raise InvalidProvidedValue('Initial number must be > 1')
    elif initial_arabic_number > 3999:
        raise InvalidProvidedValue('Initial number must be < 4000')

    result = []
    for num, rom in ARABIC_TO_ROMAN.iteritems():
        while initial_arabic_number >= num:
            initial_arabic_number -= num
            result.append(rom)
    return ''.join(result)


def roman_to_arabic(initial_roman_number):
    initial_roman_number = initial_roman_number.upper()
    result = i = 0
    for num, rom in ARABIC_TO_ROMAN.iteritems():
        l = len(rom)
        while initial_roman_number[i:i + l] == rom:
            result += num
            i += l

    if result == 0:
        raise InvalidProvidedValue('Wrong initial number')
    # `arabic_to_roman` is a way to always get the right value.
    # We should check that it's result is equal to initial value.
    # If not, the result is wrong.
    elif result > 0 and arabic_to_roman(result) != initial_roman_number:
        raise InvalidProvidedValue('Something wrong in initial number')

    return result


def choice_convert_function(number):
    # try convert to integer..
    try:
        return arabic_to_roman(int(number))
    # ..seems to be roman number
    except ValueError:
        return roman_to_arabic(number)




import re
from collections import OrderedDict, Counter


# 第二问
# convert numbers to dict  创建  using 后面的字符串 对应的字典
def convert_letters_to_number_dict(inputs=None):
    # convert letter sequence to number sequence
    if inputs and len(set(inputs)) != len(inputs):
        return None
    if inputs is None:
        inputs = "MDCLXVI"
    inputs = inputs[::-1]
    letters = []
    for index in range(0, len(inputs), 2):
        # 进行偶数位的赋值
        first_value = int(10 ** (index / 2))
        letters.append((inputs[index], first_value))
        # check 是不是4，5的位置   进行奇数位的赋值
        if index + 1 < len(inputs):
            second_value = int(5 * 10 ** (index / 2))
            letters.append((inputs[index:index + 2], second_value - first_value))
            letters.append((inputs[index + 1], second_value))
        # check是不是存在9的位置
        if index + 2 < len(inputs):
            third_value = int(10 ** ((index + 2) / 2))
            letters.append((inputs[index] + inputs[index + 2], third_value - first_value))

    # sort dictionary in reversed order
    letter_dicts = OrderedDict(reversed(letters))
    return letter_dicts


# 第二问 用上面新生成的字典  进行转换
# 罗马数字 转 阿拉伯数字
def roman_to_arabic(inputs, dicts=None):
    '''
    convert roman number to arabic number
    '''
    if dicts is None:
        dicts = convert_letters_to_number_dict()
    result = 0
    for i in range(len(inputs)):
        if inputs[i] not in dicts.keys():
            return None
        else:
            num = int(dicts[inputs[i]])
            # check if next place is larger than the current place, if so, the value should be deducted.
            if i + 1 < len(inputs) and dicts[inputs[i + 1]] > num:
                result -= num
            else:
                result += num
    # validate if it is right
    if arabic_to_roman(result, dicts) == inputs:
        return result
    else:
        return None


# 阿拉伯数字 转  罗马数字
def arabic_to_roman(initial_arabic_number, dicts):
    result = []
    for rom, num in dicts.items():
        while initial_arabic_number >= num:
            initial_arabic_number -= num
            result.append(rom)
    return ''.join(result)


# 打印输出

def convert_first(params):
    input_param = params[2]
    if re.match(r'^([1-9]|[1-3][0-9]{1,3})$', input_param):
        dicts = convert_letters_to_number_dict()
        result = arabic_to_roman(int(input_param), dicts)
    else:
        result = roman_to_arabic(input_param)

    if result:
        print(f"Sure! It is {result}")
    else:
        print(f"Hey, ask me something that's not impossible to do!")

def convert_second(params):
    if params[3] != "using":
        print("Hey, ask me something that's not impossible to do!")
    else:
        roman_dicts = convert_letters_to_number_dict(params[4])
        if roman_dicts:
            if re.match(r'^([1-9]|[1-9][0-9]+)$', params[2]):
                result = arabic_to_roman(int(params[2]), roman_dicts)
            else:
                result = roman_to_arabic(params[2], roman_dicts)
            if result:
                print(f"Sure! It is {result}")
            else:
                print("Hey, ask me something that's not impossible to do!")
        else:
            print("Hey, ask me something that's not impossible to do!")


################################
# 这是 第三问  当中 用来check 定义的规则当中  是否少值 比如少了5  50  500
# check  ABCA 这种形式 是49 的倍数
# 490/4900
# 49 abca  C 1  a 10 b 50
#
# c 1* 10**n  c = 1000

# 按照顺序 来读 10000 5000 1000  500  100  50  10  5  1

def get_next_value(letter_result, type=True):
    result = 1
    if letter_result:
        temp = max(letter_result.values())
        if type:
            if str(temp).startswith("1"):
                result = 5 * temp
            else:
                result = 2 * temp
        else:
            if str(temp).startswith("5"):
                result = temp * 2
            else:
                result = temp * 10

    return result


# 第三问
# 1.如果出现了相连续的数字
#   a.不可能出现4个连续     IIII
#   b.如果是升序，不可能出现两个连续的   I 1 X 10   IIX  VIII
#   c.如果出现2个连续的，这两个连续的一定是10幂次方 10**0  10**1
#   d.DED 肯定是19 或者是19的 10**n的数字 19*10**n
# 如果从右向左开始计算，第一个和第三个相等，那么E是1*10**n D是1 * 10**（n+1）
#   e.ABCA 罗马数字表示的最小数字49 或者是49的 10**n的数字 49*10**n
#   190   CXC

def convert_third(params):
    if params[3] != "minimally":
        print("I don't get what you want, sorry mate!")
    elif re.match(r'\d', params[2]):
        print("Hey, ask me something that's not impossible to do!")
    else:
        line = params[2][::1]
        letter_counts = Counter(line)
        letter_result = {}
        index = 0

        while index < len(line):
            first = line[index]
            # 已经处理的情况继续处理
            if first not in letter_result:
                # 判断是不是49的情况
                next_index = line.find(first, index + 1)
                # 49 case
                if next_index == index + 3:
                    start = get_next_value(letter_result, False)
                    letter_result[first] = 10 * start
                    letter_result[line[index + 1]] = start

                    letter_result[line[index + 2]] = 50 * start
                elif next_index == index + 2:
                    # 19 的情况下，应该获取的是1 或者是 10 的倍数
                    start = get_next_value(letter_result, False)
                    # 19 的情况下
                    letter_result[first] = 10 * start
                    letter_result[line[index + 1]] = start
                elif next_index == index + 1:
                    # CC 连续的情况   相等的情况，肯定是10 的倍数
                    start = get_next_value(letter_result, False)
                    letter_result[line[index + 1]] = start

                elif next_index - index > 3:
                    print("Hey, ask me something that's not impossible to do!")
                elif (index + 1) < len(line):
                    # 单个数字的
                    if letter_counts[line[index + 1]] > 1:
                        start = get_next_value(letter_result, True)
                        letter_result[line[index]] = start
                    else:
                        start = get_next_value(letter_result, True)
                        letter_result[line[index + 1]] = start

                        start = get_next_value(letter_result, False)
                        letter_result[line[index]] = start
                else:
                    # 相等的情况下 肯定是 10 的倍数
                    start = get_next_value(letter_result, True)
                    letter_result[line[index]] = start
            index += 1
        letter_result_numbers = set(letter_result.values())

        power = 0
        max_count = max(letter_result.values())

        letters = [ord(x) for x in letter_result.keys()]
        letter_index = max(letters) + 1

        while 10 ** power < max_count:
            if 1 * 10 ** power not in letter_result_numbers:
                letter_result[1 * 10 ** power] = chr(letter_index)
                letter_result_numbers.add(chr(letter_index))
                letter_index += 1
            if 5 * 10 ** power not in letter_result_numbers:
                letter_result[chr(letter_index)] = 5 * 10 ** power
                letter_result_numbers.add(5 * 10 ** power)
                letter_index += 1
            power += 1
        letter_result = dict(sorted(letter_result.items(),key = lambda x:x[1],reverse=True))
        keys = "".join(letter_result.keys())
        letter_result = convert_letters_to_number_dict(keys)
        result = roman_to_arabic(params[2],letter_result)
        print(result)

###########################################


def please_convert():
    params = input('How can I help you? ').split(" ")
    # params = "Please convert ABCADDEFGF minimally".split(" ")
    if 3 <= len(params) <= 5 and \
            params[0] == "Please" and params[1] == "convert":
        if len(params) == 3:
            convert_first(params)
        elif len(params) == 5:
            convert_second(params)
        else:
            convert_third(params)
    else:
        print("I don't get what you want, sorry mate!")


# DEFINE OTHER FUNCTIONS

please_convert()
# print(convert_letters_to_number_dict())

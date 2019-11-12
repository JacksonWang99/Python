import sys
import re
from collections import OrderedDict, Counter

prompts = input('How can I help you?')
List_prompts = str(prompts).split()
for item in List_prompts:
    if len(List_prompts) < 3:
        print("I don't get what you want, sorry mate!")
        break
    if len(List_prompts) > 5:
        print("I don't get what you want, sorry mate!")
        break
    if List_prompts[0] != "Please":
        print("I don't get what you want, sorry mate!")
        break
    if List_prompts[1] != "convert":
        print("I don't get what you want, sorry mate!")
        break
    if len(List_prompts) ==5 and List_prompts[3] != "using":
        print("I don't get what you want, sorry mate!")
        break


if len(List_prompts) == 3 and List_prompts[0] == "Please" and List_prompts[1] == "convert":
    Roman_convert_Arabic_dic = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
                                'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    Arabic_convert_Roman_dic = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
                                50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    N = List_prompts[2]

    if List_prompts[2].isdigit():
        N = List_prompts[2]
        M = int(N)
        if List_prompts[2].isdigit() and 0 < M <= 3999 and List_prompts[2][0]!= '0':
            Rom_list = []
            for key, value in Arabic_convert_Roman_dic.items():
                while M >= key:
                    M -= key
                    value = Arabic_convert_Roman_dic[key]
                    Rom_list.append(value)
                    Roman = ''.join(Rom_list)
            print(f'Sure! It is {Roman}')
        else:
            print("Hey, ask me something that's not impossible to do!")
    if List_prompts[2].isalpha():
        # 罗马数字转阿拉伯数字
        # 1.做法，从右向左，最多两位读取，再一位读取
        def Roman_convert_Arabic(N):
            count = 0
            for key in range(len(N)):
                if N[key] not in Roman_convert_Arabic_dic.keys():
                    print("Hey, ask me something that's not impossible to do!")
                    break
                else:
                    value = int(Roman_convert_Arabic_dic[N[key]])
                    position = key + 1
                    if position < len(N) and Roman_convert_Arabic_dic[N[position]] > value:
                        count -= value
                    else:
                        count += value

            return count
        count = Roman_convert_Arabic(N)

        def Double_check(count):
            Str_count = str(count)
            if Str_count.isdigit() and 0 < count <= 3999 and Str_count[0] != '0':
                Rom_list = []
                for key, value in Arabic_convert_Roman_dic.items():
                    while count >= key:
                        count -= key
                        value = Arabic_convert_Roman_dic[key]
                        Rom_list.append(value)
                        Roman = ''.join(Rom_list)
            return Roman
        Roman = Double_check(count)
        if N == str(Roman):
            print(f'Sure! It is {count}')
        else:
            print("Hey, ask me something that's not impossible to do!")
    if List_prompts[2].isalnum():
        print("Hey, ask me something that's not impossible to do!")

#第二问
elif len(List_prompts) == 5 and List_prompts[0] == 'Please' and List_prompts[1] == 'convert' \
        and List_prompts[3] == 'using':
        #and isalpha():
    List_prompts = str(prompts).split()
    Translate_Aim = List_prompts[2]  # 'XXXVI'
    Translate_Rule = List_prompts[4]  # 'XVI'
    # Reverse_Translate_Rule = list(reversed(list(Translate_Rule)))    #得到的是 一个列表 ['I', 'V', 'X']
    Reverse_Translate_Rule = Translate_Rule[::-1]  # 得到的是 字符串 'XVI'  从右往左读
    Rule_dic = {}
    # 异常情况
    #判断重复
    if Translate_Rule is None:
            Translate_Rule = "MDCLXVI"

    for index in range(0, len(Reverse_Translate_Rule), 2):
        if index % 2 == 0:
            first_value = int(10 ** (index / 2))
            Rule_dic[Reverse_Translate_Rule[index]] = first_value
        if index % 2 == 1:
            second_value = int(5 * 10 ** (index // 2))
            Rule_dic[Reverse_Translate_Rule[index]] = second_value
        # check 是不是4，5的位置
        if index + 1 < len(Reverse_Translate_Rule):
            second_value = int(5 * 10 ** (index // 2))
            Rule_dic[Reverse_Translate_Rule[index:index + 2]] = second_value - first_value
            Rule_dic[Reverse_Translate_Rule[index + 1]] = second_value
        # check是不是存在9的位置
        if index + 2 < len(Reverse_Translate_Rule):
            third_value = int(10 ** ((index + 2) / 2))
            Rule_dic[Reverse_Translate_Rule[index] + Reverse_Translate_Rule[index + 2]] = third_value - first_value

    Rule_dic = dict(sorted(Rule_dic.items(), key=lambda item: item[1], reverse=True))
    # 阿拉伯数字 转 罗马
    if Translate_Aim.isdigit() and len(Translate_Rule) == len(set(Translate_Rule)):
        Translate_Aim = List_prompts[2]
        M = int(Translate_Aim)
        if not Translate_Aim.isdigit() and M < 0 and Translate_Aim[0] == '0':
            print("Hey, ask me something that's not impossible to do!")
        else:
            Rom_list = []
            # 这里依然需要 使用 重新定义的 Rule_dic 但是 需要用 value 对应相应的 key 值 所以要进行字典  key:value  的翻转
            New_Rule_dic = {v: k for k, v in Rule_dic.items()}
            # New_Rule_dic={10: 'X', 9: 'IX', 5: 'V', 4: 'VX', 1: 'I'}
            for key, value in New_Rule_dic.items():
                while M >= key:
                    M -= key
                    value = New_Rule_dic[key]
                    Rom_list.append(value)
            print('Sure! It is ' + ''.join(Rom_list))
    # 罗马 转  阿拉伯

    elif Translate_Aim.isalpha() and len(Translate_Rule) == len(set(Translate_Rule)):
        count = 0
        for key in range(len(Translate_Aim)):
            if Translate_Aim[key] not in Rule_dic:
                print("Hey, ask me something that's not impossible to do!")
                break
            else:
                value = int(Rule_dic[Translate_Aim[key]])
                position = key + 1
                if position < len(Translate_Aim) and Rule_dic[Translate_Aim[position]] > value:
                    count -= value
                else:
                    count += value
        print(f'Sure! It is {count}')

    else:
        print("Hey, ask me something that's not impossible to do!")

#第三问
else:
    def Build_numbers(third_dict, type=True):  # third_dict 是一个字典
        result = 1
        if third_dict:  # 在这个字典当中  只有  以 1  和 5 开头的数字
            temp = max(third_dict.values())  # temp 对应的是数字  value 是数字
            if type:
                result = 5 * temp if str(temp).startswith("1") else  2 * temp
            else:
                result = temp * 2 if str(temp).startswith("5") else temp * 10
        return result


    if List_prompts[0] != "Please":
        print("I don't get what you want, sorry mate!")
    elif List_prompts[1] != "convert":
        print("I don't get what you want, sorry mate!")
    elif List_prompts[3] != "minimally":
        print("I don't get what you want, sorry mate!")
    elif len(List_prompts) != 4:
        print("I don't get what you want, sorry mate!")
    elif List_prompts[2].isalnum():
        print("Hey, ask me something that's not impossible to do!")

    else:
        list_transfar = List_prompts[2][::-1]  # 步长 为1 得到的是 ‘MMMVII’ 从后向前读
        list_transfar_counts = Counter(list_transfar)  # 对 list_transfar 中所有元素进行 计数
        third_dict = {}  # 创建的一个  字典
        list_third_dict = []
        index = 0

        while index < len(list_transfar):
            first = list_transfar[index]  # list_transfar[0]  取 第一位 ‘MMMVII’
            # 已经处理的情况继续处理
            if first not in third_dict:  # 如果 first不在 third_dict 这个字典当中
                # 判断是不是49的情况  ABCA  XLIX  这种情况   这一步是为了找  相同的元素
                next_index = list_transfar.find(first, index + 1)  # 从 下标 index +1 开始  查找第一次出现 first 子串，返回索引值
                # 49  的情况
                # 49 case   这里的index是 first : A 的索引值，判断 next_index == index + 3 是否相等，如果相等说明就是49
                if next_index == index + 3:  # 如果相同的元素间隔  是 3  说明是 49 的情况
                    # 这一步是为了确定  start 是  1  10  100 1000
                    start = Build_numbers(third_dict, False)
                    list_third_dict.append((first, 10 * start))
                    list_third_dict.append((list_transfar[index + 1], start))
                    list_third_dict.append((list_transfar[index + 2], 50 * start))
                # 19 的情况
                elif next_index == index + 2:
                    # 19 的情况下，应该获取的是1 或者是 10 的倍数  DED  19  19*10**n
                    # strat==E 肯定是1 或者10的n 次幂， 所以依然选择  False 的情况
                    start = Build_numbers(third_dict, False)
                    # 19 的情况下
                    list_third_dict.append((first, 10 * start))
                    list_third_dict.append((list_transfar[index + 1], start))
                # XX  连续的情况 10  100 1000的情况
                elif next_index == index + 1:
                    # CC 连续的情况   相等的情况 单独的一个字母  肯定是10 的倍数  10 X  100   1000
                    # 所以依然选择  False 的情况
                    start = Build_numbers(third_dict, False)
                    list_third_dict.append((list_transfar[index + 1], start))

                elif next_index - index > 3:  # 相等的两个字母的 索引值不可能超过 3  也就是 肯定是49 是最长的并且正确的罗马数字的形式
                    print("Hey, ask me something that's not impossible to do!")

                # 字母不止出现 一次的情况
                #  first 的索引值是 index  0  取过了之后  往前 一位 index+1
                elif (index + 1) < len(list_transfar):  # 这里判断的是 第二位
                    # 单个数字的
                    # list_transfar_counts = Counter(list_transfar) #对 list_transfar 中所有元素进行 计数
                    # 说明   list_transfar[index + 1] 这个字母 不止一个 并且不是 CC 19  49 上面的三种情况
                    if list_transfar_counts[list_transfar[index + 1]] > 1:
                        start = Build_numbers(third_dict, True)
                        list_third_dict.append((list_transfar[index], start))
                    else:  # list_transfar[index + 1] 这个字母 只有 一个  说明 5 5 *10**n 或者  10**n
                        start = Build_numbers(third_dict, True)
                        list_third_dict.append((list_transfar[index], start))

                        start = Build_numbers(third_dict, False)
                        list_third_dict.append((list_transfar[index + 1], start))
                else:
                    # 5  或者  10
                    start = Build_numbers(third_dict, True)
                    list_third_dict.append((list_transfar[index], start))
            for (i, j) in list_third_dict:
                third_dict[i] = j
            index += 1  # 往后 走一位

        Original_keys = "".join(third_dict.keys())
        third_dict = dict(sorted(third_dict.items(), key=lambda item: item[1], reverse=True))


        # 到这一步 完美的生成了相应的字典

        def add_extral_number(third_dict):
            power = 0
            max_count = max(third_dict.values())
            letters = [ord(x) for x in third_dict.keys()]
            letter_index = max(letters) + 1  # 72 == H
            third_dict_numbers = set(third_dict.values())
            while 10 ** power < max_count:  # 50000
                if 1 * 10 ** power not in third_dict_numbers:
                    third_dict[1 * 10 ** power] = chr(letter_index)  # 对 third_dict 进行添加更新
                    third_dict_numbers.add(chr(letter_index))
                    letter_index += 1
                if 5 * 10 ** power not in third_dict_numbers:
                    third_dict[chr(letter_index)] = 5 * 10 ** power
                    third_dict_numbers.add(5 * 10 ** power)
                    letter_index += 1
                power += 1
            return third_dict


        third_dict = add_extral_number(third_dict)
        third_dict = dict(sorted(third_dict.items(), key=lambda item: item[1], reverse=True))

        Translate_Rule = "".join(third_dict.keys())
        Reverse_Translate_Rule = Translate_Rule[::-1]

        for index in range(0, len(str(Reverse_Translate_Rule)), 2):
            if index % 2 == 0:
                first_value = int(10 ** (index / 2))
                third_dict[Reverse_Translate_Rule[index]] = first_value
            if index % 2 == 1:
                second_value = int(5 * 10 ** (index // 2))
                third_dict[Reverse_Translate_Rule[index]] = second_value
            # check 是不是4，5的位置
            if index + 1 < len(Reverse_Translate_Rule):
                second_value = int(5 * 10 ** (index // 2))
                third_dict[Reverse_Translate_Rule[index:index + 2]] = second_value - first_value
                third_dict[Reverse_Translate_Rule[index + 1]] = second_value
            # check是不是存在9的位置
            if index + 2 < len(Reverse_Translate_Rule):
                third_value = int(10 ** ((index + 2) / 2))
                third_dict[
                    Reverse_Translate_Rule[index] + Reverse_Translate_Rule[index + 2]] = third_value - first_value

        third_dict = dict(sorted(third_dict.items(), key=lambda item: item[1], reverse=True))
        N = List_prompts[2]
        count = 0
        # 罗马数字转阿拉伯数字
        # 1.做法，从右向左，最多两位读取，再一位读取
        for key in range(len(N)):
            if N[key] not in third_dict:
                print("Hey, ask me something that's not impossible to do!")
                break
            else:
                value = int(third_dict[N[key]])
                position = key + 1
                if position < len(N) and third_dict[N[position]] > value:
                    count -= value
                else:
                    count += value

        The_final_Rule = []
        for i in Translate_Rule:
            if i in Original_keys:
                The_final_Rule.append(i)
            else:
                The_final_Rule.append('_')
        print(f'Sure! It is {count} using ' + ''.join(The_final_Rule))




#if len(List_prompts) == 4:



























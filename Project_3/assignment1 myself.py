'''
相似的例子
张三说李四在说谎，李四说王五在说谎，王五说张三和李四都在说谎。现在问：这三人中到底谁说的是真话，谁说的是假话？

*问题分析与算法设计
分析题目，每个人都有可能说的是真话，也有可能说的是假话，这样就需要对每个人所说的话进行分别判断。假设三个人所说的话的真假用变量A、B、C表示，等于1表示该人说的是真话；等于0表示这个人说的是假话。由题目可以得到：
*张三说李四在说谎：
张三说的是真话（那么李四确实在说谎）：a==1&&b==0
或，张三说的是假话（那么李四没有说谎）：a==0&&b==1
*李四说王五在说谎：
李四说的是真话：b==1&&c==0
或，李四说的是假话：b==0&&c==1
*王五说张三和李四都在说谎：
王五说的是真话：c==1&&a+b==0
或，王五说的是假话：c==0&&a+b!=0
上述三个条件之间是“与”的关系。将表达式进行整理就可得到C语言的表达式：
(a&&!b||!a&&b)&&(b&&!c||!b&&c)&&(c&&a+b==0||!c&&a+b!=0)
穷举每个人说真话或说假话的各种可能情况，代入上述表达式中进行推理运算，使上述表达式均为“真”的情况就是正确的结果。

*程序说明与注释
#include <stdio.h>

void main()
{
	int a,b,c;
	for(a=0;a<=1;a++)
		for(b=0;b<=1;b++)
			for(c=0;c<=1;c++)
				if((a&&!b||!a&&b)&&(b&&!c||!b&&c)&&(c&&a+b==0||!c&&a+b!=0))
				{
					printf("Zhangsan told a %s.\n",a?"truth":"lie");
					printf("Lisi told a %s.\n",b?"truch":"lie");
					printf("Wangwu told a %s.\n",c?"truch":"lie");
				}
}

*运行结果
Zhangsan told a lie.
Lisi told a truch.
Wangwu told a lie.
'''
# get the input
import re
filename = input('Which text file do you want to use for the puzzle?')
# 使用 with  open 进行打开
with open(filename,'r') as files:
    text = files.read()

# 把陈述句子两边加上*，后期好解析陈述
    sentences = text.replace('\n',' ').replace('."','*.').replace('?"','*.').replace('!"','*.').replace(',"','*').replace('"','*')
    sentences = re.split('\.',sentences)[:-1]


#创建 namelist 列表进行比较
namelist = []
nwant = ['Yesterday,', 'Then', 'I','Sir','Sirs', 'Knaves', 'Knave', 'Knights', 'Knight']
for line in sentences:
    wordlist = line.split()
    print(wordlist)
    for word in wordlist:
        if word.strip('*') not in nwant and list(word)[0].isupper():
            namelist.append(word.strip('*').strip(',').strip('!'))
namelist = sorted(set(namelist))

'''
第一步：需要把对应人和陈述全部提出来. 做成一个字典{'name': 'formated staments'}
第二步：把人的陈诉规范化
第三步：确定逻辑
'''
pattern = "\*(.+)\*"
staments_pairs = {}
for name in namelist:
    staments_pairs[name] = ''  #依次判断namelist里面的名字
for line in sentences:        #这里是把真正说出来的话打印了出来，有具体的内容的话
    if '*' in line:
        print(line)
        stament = re.findall("\*(.+)\*",line)     #stament 是指 这里是把 说的话 单独拿出来
        print(stament)
        if stament != []:                    #如果 statement 不是空 下面判断谁说了什么
            # 知道陈述是谁说的
            for name in namelist:
                if (name in line) & (name not in stament[0]):
                    whosay = name
                                  #whosay 是指谁说话了
           #获得陈述放进staments_pairs，进行名字和内容的匹配
            if 'I'in stament[0]:            #如果在说的话第一位是I，那么把I替换成 说话的人speaker
                stament[0] =stament[0].replace('I',whosay)
            staments_pairs[whosay]  = stament[0]

# 规范化 三个文档就三种话: A是* ,  A和B是*, at least one of Sir Hilary and I is a Knave.

for whosay, stament in staments_pairs.items():  # 在这里 staments_pairs 是一个字典 使用 items()进行遍历，访问每一个值
    if 'are Knaves' in stament:  # stament 是指之前的人说的话这里是把说的话 单独拿出来，当 are Knaves 在stament当中的时候
        intername = []
        for word in stament.split():  # split 指定分隔符对字符串进行切片, word 指这句话中的每一个单词
            if word.istitle() and (word not in nwant):  # .istitle() 如果字符串中所有的单词拼写首字母是否为大写，
                intername.append(word)  # 且其他字母为小写则返回 True，否则返回 False.#如果 word首字母是大写，并且 word 不在 nwant列表中
        staments_pairs[whosay] = '(({}&(({})==0))|(~{}&(({})!=0)))'.format(whosay, '+'.join(intername), whosay,
                                                                           '+'.join(intername))
    # 转化  ，把 statement_pairs 里的内容转变成上述格式.
    if 'at least' in stament:
        intername = []
        for word in stament.split():
            if word.istitle() and (word not in nwant):
                intername.append(word)
        print(intername)
        staments_pairs[whosay] = '(({}&({}&~{}==1))|(~{}&(~{}==1&{}==1)))'.format(
            whosay, whosay, intername[0], whosay, whosay, intername[0])

    if 'am a Knight' in stament:
        intername = []
        for word in stament.split():
            if word.istitle() and (word not in nwant):
                intername.append(word)
        staments_pairs[whosay] = 'True'

    if 'am a Knave' in stament:
        intername = []
        for word in stament.split():
            if word.istitle() and (word not in nwant):
                intername.append(word)
        staments_pairs[whosay] = 'False'
    if stament == '':  # stament 是指之前的人说的话这里是把说的话 单独拿出来，
        # 当整个列表为空的时候，也就是没人说活的时候 ，等于true
        staments_pairs[whosay] = 'True'

judge = '&'.join(staments_pairs.values())

condition = []
role_pairs = []
if len(namelist) == 2:
    for a1 in [0, 1]:
        locals()[namelist[0]] = a1
        for a2 in [0, 1]:
            locals()[namelist[1]] = a2
            if eval(judge) == 1:
                condition.append([eval(namelist[0]), eval(namelist[1])])

if len(namelist) == 3:
    for a1 in [0, 1]:
        locals()[namelist[0]] = a1
        for a2 in [0, 1]:
            locals()[namelist[1]] = a2
            for a3 in [0, 1]:
                locals()[namelist[2]] = a3
                if eval(judge) == 1:
                    condition.append([eval(namelist[0]), eval(namelist[1]), eval(namelist[2])])

if len(namelist) == 4:
    for a1 in [0, 1]:
        locals()[namelist[0]] = a1
        for a2 in [0, 1]:
            locals()[namelist[1]] = a2
            for a3 in [0, 1]:
                locals()[namelist[2]] = a3
                for a4 in [0, 1]:
                    locals()[namelist[3]] = a4
                    if eval(judge) == 1:
                        condition.append([eval(namelist[0]), eval(namelist[1]), eval(namelist[2]), eval(namelist[3])])

len(condition)
print('The Sirs are: ' + ' '.join(namelist))
if condition == []:
    print('There is no solution.')

if len(condition) == 1:
    print('There is a unique solution:')

    flat_list = sum(condition, [])
    for index in range(len(flat_list)):
        if flat_list[index] == 0:
            flat_list[index] = 'Knave'
        elif flat_list[index] == 1:
            flat_list[index] = 'Knight'
    for i in range(len(namelist)):
        print('Sir {} is a {}.'.format(namelist[i], flat_list[i]))

if len(condition) > 1:
    print('There are {} solutions.'.format(len(condition)))
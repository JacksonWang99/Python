# Written by *** and Eric Martin for COMP9021


def rule_encoded_by(rule_nb):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    '''
    values = [int(d) for d in f'{rule_nb:04b}']
    return {(p // 2, p % 2): values[p] for p in range(4)}


def describe_rule(rule_nb):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    '''
    rule = rule_encoded_by(rule_nb)
    print('The rule encoded by', rule_nb, 'is: ', rule)
    print()
    for i, j in rule.items():
        print ('After {} followed by {}, we draw {}'.format(i[0],i[1],j))
    # INSERT YOUR CODE HERE TO PRINT 4 LINES

    for i,j  in rule.items():
        print ('After {} followed by {}, we draw value {}'.format(i[0],i[1],j))

def draw_line(rule_nb, first, second, length):
        # 解释一下 rule_nb 就是上面提到的那一串字符串，
        #         first,second  要么是1 或者是 0
        #         length 是长度，长度是多上就输出多少个字符
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    "first" and "second" are supposed to be the integer 0 or the integer 1.
    "length" is supposed to be a positive integer (possibly equal to 0).

    
    Draws a line of length "length" consisting of 0's and 1's,
    that starts with "first" if "length" is at least equal to 1,
    followed by "second" if "length" is at least equal to 2,
    and with the remaining "length" - 2 0's and 1's determined by "rule_nb".
    '''
    rule = rule_encoded_by(rule_nb)
 

    if length== 0:
                print ('')
    if length== 1:
                print(str(first))		
    if length== 2:
                print(str(first)+str(second))
    if length>  2:
        line=[first,second]
        for i in range(length-2):
            s=line[-2:]
            line.append(rule[(int(s[0]),int(s[1]))])
        line2=''
        for i in line:
            line2+=str(i)
        print (line2)

def cone_line(rule_nb, first, second, length):
        # 解释一下 rule_nb 就是上面提到的那一串字符串，
        #         first,second  要么是1 或者是 0
        #         length 是长度，长度是多上就输出多少个字符
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    "first" and "second" are supposed to be the integer 0 or the integer 1.
    "length" is supposed to be a positive integer (possibly equal to 0).

    
    Draws a line of length "length" consisting of 0's and 1's,
    that starts with "first" if "length" is at least equal to 1,
    followed by "second" if "length" is at least equal to 2,
    and with the remaining "length" - 2 0's and 1's determined by "rule_nb".
    '''
    rule = rule_encoded_by(rule_nb)
 

    if length== 0:
                print ('')
    if length== 1:
                print(str(first))       
    if length== 2:
                print(str(first)+str(second))
    if length>  2:
        line=[first,second]
        for i in range(length-2):
            s=line[-2:]
            line.append(rule[(int(s[0]),int(s[1]))])
        line2=''
        for i in line:
            line2+=str(i)
        return line2
    # INSERT YOUR CODE HERE TO PRINT ONE LINE


def uniquely_produced_by_rule(line):
    '''
    "line" is assumed to be a string consisting of nothing but 0's and 1's.

    Returns an integer n between 0 and 15 if the rule encoded by n is the
    UNIQUE rule that can produce "line"; otherwise, returns -1.
    '''
   

    line3=[]
    line4=[]
    for i in range(16):
        line3.append(cone_line(i, int(line[0]), int(line[1]), len(line)))
    for i in range (16):
        if line==line3[i]:
            line4.append(i)

    if len(line4) == 1:
        return line4[0]
    else:
        return '-1'
    
        
    # REPLACE pass ABOVE WITH YOUR CODE

print(uniquely_produced_by_rule('001101101'))

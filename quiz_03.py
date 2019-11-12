import sys

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
      )
print()


def direction_selection_number(item, point_x, point_y):
    if item == '0':
        point_x = point_x
        point_y = point_y - 1
    if item == '1':
        point_x = point_x - 1
        point_y = point_y - 1
    if item == '2':
        point_x = point_x - 1
        point_y = point_y
    if item == '3':
        point_x = point_x - 1
        point_y = point_y + 1
    if item == '4':
        point_x = point_x
        point_y = point_y + 1
    if item == '5':
        point_x = point_x + 1
        point_y = point_y + 1
    if item == '6':
        point_x = point_x + 1
        point_y = point_y
    if item == '7':
        point_x = point_x + 1
        point_y = point_y - 1
    return point_x, point_y


def draw_points(A, B, C, D):
    lines = []
    for y in range(C, D):  # 代表了行
        line = []
        for x in range(A, B):
            if (x, y) in Dot:
                line.append(on)
            else:
                line.append(off)
        lines.append(reversed(line))
    return lines


num = '0' * nb_of_leading_zeroes + f'{int(code):o}'
start_x, start_y = (0, 0)
Dot = {(0, 0): 1}

# 从右往左读
# 0256   0400
# 这里是否可以 封装成一个 Dot 的函数
keys = []
for item in num[::-1]:
    start_x, start_y = direction_selection_number(item, start_x, start_y)
    # start_x ,start_y 是 0 1 的元组
    if (start_x, start_y) not in Dot:
        Dot[(start_x, start_y)] = 1
    else:
        if Dot[(start_x, start_y)] == 1:
            Dot[(start_x, start_y)] = 0
        else:
            Dot[(start_x, start_y)] = 1
    # for i, j in Dot.items():
        # keys.append(i)  # 这里的keys = []

for i,j in Dot.items():
    if j == 1:
        keys.append(i);

if keys:
    List_x = []
    List_y = []
    Tuple_x = ()
    Tuple_y = ()
    for (x, y) in keys:
        List_x.append(x)
        List_y.append(y)
        Tuple_x = tuple(List_x)
        Tuple_y = tuple(List_y)
    x_min = min(Tuple_x)
    x_max = max(Tuple_x)
    y_min = min(Tuple_y)
    y_max = max(Tuple_y)

    A = x_min
    B = x_max + 1
    C = y_min
    D = y_max + 1

    for i in draw_points(A, B, C, D):
        for j in i:
            print(j, end='')
        print()

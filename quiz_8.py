# Creates 3 classes, Point, Line and Parallelogram.
# A point is determined by 2 coordinates (int or float).
# A line is determined by 2 distinct points.
# A parallelogram is determined by 4 distinct lines,
# two of which having the same slope, the other two
# having the same slope too.
# The Parallelogram class has a method, divides_into_two_parallelograms(),
# that determines where a line, provide as arguments, can split
# the object into two smaller parallelograms.
#
# Written by *** for COMP9021


from collections import defaultdict


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self,other):
        if self.x == other.x and self.y ==other.y:
            return True
        else:
            return False


# Define a class to raise Line errors

class LineError(Exception):
    def __init__(self, message):
        self.message = message


class Line:
    def __init__(self, dot1, dot2):
        self.start = dot1
        self.end = dot2
        if dot1 == dot2:
            raise LineError('Cannot create line')
        if dot1.y == dot2.y: # 水平直线斜率为 0
            self.slop == 0
        elif dot1.x == dot2.x: # 垂直直线  斜率不存在
            self.slop = None
        else:
            self.slop = (dot1.y - dot2.y) * 1.0 / (dot1.x - dot2.x)

    def __eq__(self, new):
        if self.start == new.start and self.end == new.end:
            return True
        if self.start == new.end and self.end == new.start:
            return True
        return False


class ParallelogramError(Exception):
    def __int__(self, message):
        self.message = message


class Parallelogram:
    def __init__(self, line1, line2, line3, line4):
        self.lines = [line1, line2, line3, line4]

        slops = defaultdict(int) #  defaultdict(int)意味着 生成的 slops 这个字典的value 值默认是int 型

        for item in self.lines:
            slops[item.slop] += 1

        for item in self.lines:
            check_list = []
            if item not in check_list:
                check_list.append(item)
            else:
                raise ParallelogramError('Cannot create parallelogram')

        if len(slops) != 2:
            raise ParallelogramError('Cannot create parallelogram')

        for value in slops.values():
            if value != 2:
                raise ParallelogramError('Cannot create parallelogram')

    def __eq__(self, line1, line2, line3, line4):

        self.lines = [line1, line2, line3, line4]

        # if len(self.lines) != len(list(set(self.lines))):
        # return False
        check_list = []
        for item in self.lines:
            if item not in check_list:
                check_list.append(item)
            else:
                raise ParallelogramError('Cannot create parallelogram')


    # Replace pass above with your code

    def divides_into_two_parallelograms(self, line):

        if line in self.lines:
            return False
        for exit_line in self.lines:
            if exit_line.slop == line.slop:
                return True
        return False
        # Replace pass above with your code


pt_11 = Point(-2, 5)
pt_12 = Point(6, 1)
pt_21 = Point(0, 6)
pt_22 = Point(-1, 0)
pt_31 = Point(2, -1)
pt_32 = Point(3, 5)
pt_41 = Point(-3, 3)
pt_42 = Point(1, 1)

line_1 = Line(pt_11, pt_12)
line_2 = Line(pt_21, pt_22)
line_3 = Line(pt_31, pt_32)
line_4 = Line(pt_41, pt_42)

line = Line(Point(4, -2), Point(6, 10))

parallelogram = Parallelogram(line_1, line_2, line_3, line_1)

print(parallelogram)

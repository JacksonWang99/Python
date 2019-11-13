from xml.dom.minidom import parse
from os.path import realpath
from numpy import arange, cross, array
from math import pi, cos, sin


def available_coloured_pieces(file):
    coloured_pieces = {}
    for piece in parse(realpath(file.name)).documentElement.getElementsByTagName("path"):
        coloured_pieces[piece.getAttribute('fill')] = \
            ColoredPiece([(int(x.strip().split(' ')[0]), int(x.strip().split(' ')[1]))
                          for x in (piece.getAttribute('d').replace('M', '')).replace('z', '').split('L')])
    return coloured_pieces


def are_valid(coloured_pieces):
    if len(coloured_pieces) == 0:
        return False
    for coloured_piece in coloured_pieces.values():
        if not coloured_piece.is_valid():
            return False
    return True


def are_identical_sets_of_coloured_pieces(coloured_pieces_1, coloured_pieces_2):
    for color in coloured_pieces_1.keys():
        if color not in coloured_pieces_2.keys():
            return False
        if not coloured_pieces_1[color].is_same(coloured_pieces_2[color]):
            return False
    return True


def is_solution(tangram, shape):
    shape = shape[list(shape.keys())[0]]

    tangram_area = sum([abs(x.piece.area()) for x in tangram.values()])

    if abs(shape.piece.area()) != tangram_area:
        return False

    tangram = list(tangram.values())

    point_num_shape = len(shape.points_list)

    for i in range(point_num_shape):
        edges = [shape.points_list[i], shape.points_list[(i + 1) % point_num_shape]]
        for x in tangram:
            if x.piece.intersection(edges) != []:
                return False

    for x in tangram:
        if not x.is_contain(shape):
            return False

    for x in range(len(tangram)):
        for y in range(x + 1, len(tangram)):
            if sorted(tangram[x].points_list) == sorted(tangram[y].points_list):
                return False
            if not tangram[x].is_disjoint(tangram[y]):
                return False

    return True


class ColoredPiece:

    def __init__(self, points_list):
        self.points_list = points_list
        self.points_list_mirr_x = [(x, -y) for (x, y) in points_list]
        self.points_list_mirr_y = [(-x, y) for (x, y) in points_list]
        self.points_set = list(set(self.points_list))
        self.piece = MyPolygon(points_list)
        self.piece_mirr_x = MyPolygon(self.points_list_mirr_x)
        self.piece_mirr_y = MyPolygon(self.points_list_mirr_y)

    def vertices_number(self):
        return len(self.points_list)

    def is_valid(self):
        argment_points_list = [self.points_list[-1]] + self.points_list
        for i in range(len(argment_points_list) - 1):
            for j in range(len(argment_points_list) - 1):
                if i != j:
                    A = (argment_points_list[i][0], argment_points_list[i][1])
                    B = (argment_points_list[i + 1][0], argment_points_list[i + 1][1])
                    C = (argment_points_list[j][0], argment_points_list[j][1])
                    D = (argment_points_list[j + 1][0], argment_points_list[j + 1][1])

                    if is_fold([A, B], [C, D]):
                        return False

                    P = getCrossPoint([A, B], [C, D])
                    if P == None:
                        continue
                    if not (P in [A, B, C, D]):
                        return False
        return self.piece.is_convex()

    def is_same(self, o):
        if not abs(self.piece.area()) == abs(o.piece.area()):
            return False
        if not self.vertices_number() == o.vertices_number():
            return False
        p0 = translation_to_centroid(self.piece).points_list
        for rad in arange(-pi, pi, pi / 2):
            p2 = translation_to_centroid(o.piece.rotate(rad)).points_list
            if sorted(p0) == sorted(p2):
                return True
        for rad in arange(-pi, pi, pi / 2):
            p2 = translation_to_centroid(o.piece_mirr_x.rotate(rad)).points_list
            if sorted(p0) == sorted(p2):
                return True
        for rad in arange(-pi, pi, pi / 2):
            p2 = translation_to_centroid(o.piece_mirr_y.rotate(rad)).points_list
            if sorted(p0) == sorted(p2):
                return True
        return False

    def is_disjoint(self, o):
        for v in o.piece.points_list:
            if self.piece.encloses_point(v):
                flag = True
                for i in range(len(self.points_list)):
                    A = self.points_list[i]
                    B = self.points_list[(i + 1) % len(self.points_list)]
                    C = v
                    if is_fold([A, B], [B, C]) or C in [A, B]:
                        flag = False
                        break
                if flag:
                    return False
        for v in self.piece.points_list:
            if o.piece.encloses_point(v):
                flag = True
                for i in range(len(o.points_list)):
                    A = o.points_list[i]
                    B = o.points_list[(i + 1) % len(o.points_list)]
                    C = v
                    if is_fold([A, B], [B, C]) or C in [A, B]:
                        flag = False
                        break
                if flag:
                    return False

        argment_points_list = [self.points_list[-1]] + self.points_list
        argment_points_list2 = [o.points_list[-1]] + o.points_list
        flag = 0
        for i in range(len(argment_points_list) - 1):
            A = argment_points_list[i]
            B = argment_points_list[i + 1]
            for j in range(len(argment_points_list2) - 1):
                C = argment_points_list2[j]
                D = argment_points_list2[j + 1]
                if is_fold2([A, B], [C, D]):
                    flag += 1
                    if flag == 2:
                        return False
        return True

    def is_contain(self, o):

        X = 0
        Y = 0
        l = len(self.piece.points_list)
        for i in range(l):
            X += self.piece.points_list[i][0]
            Y += self.piece.points_list[i][1]

        X = X // l
        Y = Y // l

        for v in self.piece.points_list + [(X,Y)]:
            if not o.piece.encloses_point(v):
                flag = True
                for i in range(len(o.points_list)):
                    A = o.points_list[i]
                    B = o.points_list[(i + 1) % len(o.points_list)]
                    C = v
                    if ( is_fold([A,B],[B,C]) and onLine(C,[A,B])) or C in [A, B]:
                        flag = False
                        break
                if flag:
                    return False



        return True


# helper function
def translation_to_centroid(piece):
    X = 0
    Y = 0
    l = len(piece.points_list)
    for i in range(l):
        X += piece.points_list[i][0]
        Y += piece.points_list[i][1]

    X = X // l
    Y = Y // l

    return piece.translate(-X, -Y)


def n_rotate(angle, valuex, valuey, pointx, pointy):
    valuex = array(valuex)
    valuey = array(valuey)
    nRotatex = (valuex - pointx) * cos(angle) - (valuey - pointy) * sin(angle) + pointx
    nRotatey = (valuex - pointx) * sin(angle) + (valuey - pointy) * cos(angle) + pointy
    return (round(nRotatex), round(nRotatey))


class MyPolygon:
    def __init__(self, points_list):
        self.points_list = points_list

    def vertices_number(self):
        return len(self.points_list)

    def encloses_point(self, A):
        x = A[0]
        y = A[1]
        inf = 10000

        result = False
        for i in range(len(self.points_list) - 1):
            if intersect((self.points_list[i][0], self.points_list[i][1]),
                         (self.points_list[i + 1][0], self.points_list[i + 1][1]),
                         (x, y), (inf, y)):
                result = not result
        if intersect((self.points_list[-1][0], self.points_list[-1][1]),
                     (self.points_list[0][0], self.points_list[0][1]), (x, y),
                     (inf, y)):
            result = not result
        return result

    def intersection(self, p):
        C = p[0]
        D = p[1]
        argment_points_list = [self.points_list[-1]] + self.points_list
        tmp = []
        for i in range(len(argment_points_list) - 1):
            A = (argment_points_list[i][0], argment_points_list[i][1])
            B = (argment_points_list[i + 1][0], argment_points_list[i + 1][1])
            P = getCrossPoint([A, B], [C, D])
            if P == None:
                continue
            if not (P in [A, B, C, D]):
                tmp.append(P)
        return tmp

    def is_convex(self):
        argment_points_list = [self.points_list[-1]] + self.points_list + [self.points_list[0]]
        tmp = []
        for i in range(len(argment_points_list) - 2):
            A = argment_points_list[i]
            B = argment_points_list[i + 1]
            C = argment_points_list[i + 2]
            BA = [A[0] - B[0], A[1] - B[1], 0]
            BC = [C[0] - B[0], C[1] - B[1], 0]
            c = cross(BA, BC)
            if c[0] == 0 and c[1] == 0 and c[2] == 0:
                return False
            if cross(BA, BC)[-1] > 0:
                tmp.append(1)
            else:
                tmp.append(-1)

        if len(set(tmp)) == 1:
            return True
        else:
            return False

    def translate(self, X, Y):
        tmp = []
        for i in range(len(self.points_list)):
            tmp.append((self.points_list[i][0] + X, self.points_list[i][1] + Y))
        return MyPolygon(tmp)

    def rotate(self, angle):
        tmp = []
        for i in range(len(self.points_list)):
            tmp.append(n_rotate(angle, self.points_list[i][0], self.points_list[i][1], 0, 0))

        return MyPolygon(tmp)

    def area(self):
        point_num = len(self.points_list)
        if point_num < 3:
            return 0

        s = 0
        for i in range(point_num):
            s += self.points_list[i][0] * self.points_list[(i + 1) % point_num][1] - \
                 self.points_list[i][1] * self.points_list[(i + 1) % point_num][0]
        return abs(s / 2)

    def vertices(self):
        return len(self.points_list)


def inSegment(p, line, line2):
    if line[0][0] == line[1][0]:
        if p[1] > min(line[0][1], line[1][1]) and p[1] < max(line[0][1], line[1][1]):
            if p[0] > min(line2[0][0], line2[1][0]) and p[0] < max(line2[0][0], line2[1][0]):
                return True
    elif line[0][1] == line[1][1]:
        if p[0] > min(line[0][0], line[1][0]) and p[0] < max(line[0][0], line[1][0]):
            if p[1] > min(line2[0][1], line2[1][1]) and p[1] < max(line2[0][1], line2[1][1]):
                return True
    else:
        if p[0] > min(line[0][0], line[1][0]) and p[0] < max(line[0][0], line[1][0]):
            if p[1] > min(line2[0][1], line2[1][1]) and p[1] < max(line2[0][1], line2[1][1]) and p[0] > min(
                    line2[0][0], line2[1][0]) and p[0] < max(line2[0][0], line2[1][0]):
                return True
    return False


def is_fold(line1, line2):
    a1, b1, c1 = getLinePara(line1)
    a2, b2, c2 = getLinePara(line2)
    aa1 = a1 if a1 != 0 else (b1 if b1 != 0 else c1)
    aa2 = a2 if a2 != 0 else (b2 if b2 != 0 else c2)
    if a1 * aa2 == a2 * aa1 and b1 * aa2 == b2 * aa1 and c1 * aa2 == c2 * aa1:
        return True
    return False


def is_fold2(line1, line2):
    a1, b1, c1 = getLinePara(line1)
    a2, b2, c2 = getLinePara(line2)
    aa1 = a1 if a1 != 0 else (b1 if b1 != 0 else c1)
    aa2 = a2 if a2 != 0 else (b2 if b2 != 0 else c2)
    if a1 * aa2 == a2 * aa1 and b1 * aa2 == b2 * aa1 and c1 * aa2 == c2 * aa1:
        if not (line1[0] in line2) and onLine(line1[0], line2):
            return True
        if not (line1[1] in line2) and onLine(line1[1], line2):
            return True
        if not (line2[0] in line1) and onLine(line2[0], line1):
            return True
        if not (line2[1] in line1) and onLine(line2[1], line1):
            return True

    return False


def onLine(P,line):
    A = line[0]
    B = line[1]
    PA = (A[0]-P[0], A[1]-P[1])
    PB = (B[0] - P[0], B[1] - P[1])
    t = PA[0]*PB[0] + PA[1]*PB[1]
    if t > 0:
        return False
    else:
        return True

def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])


# Return true if line segments AB and CD intersect
def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def getLinePara(line):
    a = line[0][1] - line[1][1]
    b = line[1][0] - line[0][0]
    c = line[0][0] * line[1][1] - line[1][0] * line[0][1]
    return a, b, c


def getCrossPoint(line1, line2):
    a1, b1, c1 = getLinePara(line1)
    a2, b2, c2 = getLinePara(line2)
    d = a1 * b2 - a2 * b1
    p = [0, 0]
    if d == 0:
        return None
    else:
        p[0] = (b1 * c2 - b2 * c1) * 1.0 / d
        p[1] = (c1 * a2 - c2 * a1) * 1.0 / d
    p = tuple(p)
    if inSegment(p, line1, line2):
        return p
    else:
        return None


'''
print(are_valid(available_coloured_pieces(open('incorrect_pieces_4.xml'))))

# are_identical_sets_of_coloured_pieces(available_coloured_pieces(open('pieces_A.xml')),
#                                      available_coloured_pieces(open('pieces_AA.xml')))

file = open('B-shape.xml')
shape = available_coloured_pieces(file)
file = open('B-not-solution-invalid-outside.xml')
tangram = available_coloured_pieces(file)
print(is_solution(tangram, shape))
'''



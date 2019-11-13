from xml.dom.minidom import parse
from os.path import realpath
from sympy.geometry import *
from numpy import arange
from math import pi


def available_coloured_pieces(file):
    coloured_pieces = {}
    for piece in parse(realpath(file.name)).documentElement.getElementsByTagName("path"):
        coloured_pieces[piece.getAttribute('fill')] = \
            ColoredPiece([(Point2D(int(x.strip().split(' ')[0]), int(x.strip().split(' ')[1])))
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

    tangram_area = sum([abs(x.piece.area) for x in tangram.values()])

    if abs(shape.piece.area) != tangram_area:
        return False

    tangram = list(tangram.values())
    for x in tangram:
        if not x.is_contain(shape):
            return False

    for x in range(len(tangram)):
        for y in range(x+1,len(tangram)):

            if tangram[x] == tangram[y]:
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
        self.piece = Polygon(*points_list)
        self.piece_mirr_x = Polygon(*self.points_list_mirr_x)
        self.piece_mirr_y = Polygon(*self.points_list_mirr_y)

    def vertices_number(self):
        return len(self.piece.vertices)

    def centroid(self):
        return (self.piece.centroid.x, self.piece.centroid.y)

    def is_valid(self):
        if isinstance(self.piece, Segment2D) or isinstance(self.piece, Point2D):
            return False
        if not self.vertices_number() == len(self.points_set):
            return False
        if not self.piece.is_convex():
            return False
        return True

    def is_same(self, o):
        if not abs(self.piece.area) == abs(o.piece.area):
            return False
        if not self.vertices_number() == o.vertices_number():
            return False
        p0 = translation_to_centroid(self.piece)
        for rad in arange(-pi, pi, pi / 2):
            p2 = translation_to_centroid(o.piece.rotate(rad))
            if p0 == p2:
                return True
        for rad in arange(-pi, pi, pi / 2):
            p2 = translation_to_centroid(o.piece_mirr_x.rotate(rad))
            if p0 == p2:
                return True
        for rad in arange(-pi, pi, pi / 2):
            p2 = translation_to_centroid(o.piece_mirr_y.rotate(rad))
            if p0 == p2:
                return True
        return False

    def is_disjoint(self,o):
        for v in self.piece.vertices:
            if self.piece.encloses_point(v):
                return False
        for e1 in self.piece.sides:
            for e2 in o.piece.sides:
                tmp = e1.intersection(e2)
                if len(tmp) > 0:
                    if tmp[0].is_Point and not tmp[0] in [e1.p1,e1.p2,e2.p1,e2.p2]:
                        return False
            if len(o.piece.intersection(e1)) >= 2:
                return False
        return True

    def is_contain(self,o):
        for v in self.piece.vertices:
            if not o.piece.encloses_point(v) and o.piece.intersection(v) == []:
                return False

        if not (o.piece.encloses_point(self.piece.centroid)):
            return False

        return True

# helper function
def translation_to_centroid(piece):
    return piece.translate(-piece.centroid.x, -piece.centroid.y)

import math


class PolygonsError(Exception):
    def __init__(self, info):
        super().__init__(self)
        self.errorinfo = info

    def __str__(self):
        return self.errorinfo


class Polygons:
    def __init__(self, file_name):
        self.name = file_name[:-4]
        self.matrix = []
        self.rs = 0
        self.cs = 0
        self.close_table = []
        self.end_flag = 0
        self.contours = []
        self.path_rec = []

        file_object = open(file_name)

        try:
            for line in file_object:
                tmp = []
                for c in line:
                    if not (c == ' ' or c == '\n'):
                        i = int(c)
                        if i == 1 or i == 0:
                            tmp.append(i)
                        else:
                            raise PolygonsError("Incorrect input.")
                if not (tmp == []):
                    tmp.insert(0, 0)
                    tmp.append(0)
                    self.matrix.append(tmp)
            self.cs = len(self.matrix[0])

            tmp = [0 for _ in range(self.cs)]
            self.matrix.append(tmp)
            self.matrix.insert(0, tmp)

            self.rs = len(self.matrix)
            self.cs = len(self.matrix[0])
            if not (self.rs > 4 and self.cs > 4 and self.rs <= 52 and self.cs <= 52):
                raise PolygonsError("Incorrect input.")

        except FileNotFoundError:
            pass
        finally:
            file_object.close()

        flag = True
        while flag:
            flag_1 = False
            for i in range(1, self.rs):
                for j in range(1, self.cs):
                    if self.matrix[i][j] == 1:
                        contour = self._contour((i, j))
                        if not (contour is None or contour == []):
                            self.contours.append(contour)
                            for p in contour:
                                self.matrix[p[0]][p[1]] = 0
                            flag_1 = True
                    if flag_1:
                        break
                if flag_1:
                    break
            if not flag_1:
                flag = False

        if len(self.contours) == 0:
            raise PolygonsError("Cannot get polygons as expected.")

        for i in range(1, self.rs):
            for j in range(1, self.cs):
                if self.matrix[i][j] == 1:
                    raise PolygonsError("Cannot get polygons as expected.")

        self.perimeters = [0 for _ in range(len(self.contours))]
        self.areas = [0 for _ in range(len(self.contours))]
        self.convexes = [0 for _ in range(len(self.contours))]
        self.rotations = [0 for _ in range(len(self.contours))]
        self.depths = [0 for _ in range(len(self.contours))]

        self._perimeters()
        self._areas()
        self._convexes()
        self._rotations()
        self._depths()

    def _contour(self, p):
        directions = []
        if self.matrix[p[0]][p[1] + 1] == 1:
            directions.append((p[0], p[1] + 1))
        if self.matrix[p[0] + 1][p[1] + 1] == 1:
            directions.append((p[0] + 1, p[1] + 1))
        if self.matrix[p[0] + 1][p[1]] == 1:
            directions.append((p[0] + 1, p[1]))
        if not (directions == []):
            self.end_flag = 0
            self.path_rec = []
            self._path([p, directions[0]])
            return self.path_rec

    def _path(self, path):
        if self.end_flag == 0:
            all_dir = self._directions(path[-1], path)
            if path[0] == path[-1]:
                self.end_flag = 1
                for d in path:
                    self.path_rec.append(d)
                return self.path_rec
            else:
                for dir in all_dir:
                    new_path = []
                    for d in path:
                        new_path.append(d)
                    new_path.append(dir)
                    self._path(new_path)

    def _directions(self, p, path):
        dir = [(p[0], p[1] - 1), (p[0] - 1, p[1] - 1), (p[0] - 1, p[1]), (p[0] - 1, p[1] + 1), (p[0], p[1] + 1),
               (p[0] + 1, p[1] + 1), (p[0] + 1, p[1]),
               (p[0] + 1, p[1] - 1)]
        [p1, p2] = path[-2:]
        new_dir = []
        if (p2[0] - p1[0], p2[1] - p1[1]) == (0, -1):
            new_dir = dir[5:]
            new_dir.extend(dir[0:4])
        elif (p2[0] - p1[0], p2[1] - p1[1]) == (-1, -1):
            new_dir = dir[6:]
            new_dir.extend(dir[0:5])
        elif (p2[0] - p1[0], p2[1] - p1[1]) == (0, 1):
            new_dir = dir[1:]
            new_dir.extend([dir[0]])
        elif (p2[0] - p1[0], p2[1] - p1[1]) == (-1, 0):
            new_dir = [dir[7]]
            new_dir.extend(dir[0:6])
        elif (p2[0] - p1[0], p2[1] - p1[1]) == (1, 0):
            new_dir = dir[3:]
            new_dir.extend(dir[0:2])
        elif (p2[0] - p1[0], p2[1] - p1[1]) == (-1, 1):
            new_dir = dir
        elif (p2[0] - p1[0], p2[1] - p1[1]) == (1, -1):
            new_dir = dir[4:]
            new_dir.extend(dir[0:3])
        elif (p2[0] - p1[0], p2[1] - p1[1]) == (1, 1):
            new_dir = dir[2:]
            new_dir.extend(dir[0:1])
        new_directions = []
        if not (new_dir == []):
            for nd in new_dir:
                if self.matrix[nd[0]][nd[1]] == 1 and not (self._inPath(nd, path[1:])):
                    new_directions.append(nd)
        return new_directions

    def _inPath(self, p, path):
        for pc in path:
            if pc == p:
                return True
        return False

    def _nodes(self, contour):
        node = [(contour[0][1] - 1, contour[0][0] - 1)]
        for i in range(1, len(contour[:-1])):
            x1 = node[-1][0]
            y1 = node[-1][1]
            x2 = contour[i][1] - 1
            y2 = contour[i][0] - 1
            x3 = contour[i + 1][1] - 1
            y3 = contour[i + 1][0] - 1
            if not ((y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)):
                node.append((contour[i][1] - 1, contour[i][0] - 1))

        x1 = node[-1][0]
        y1 = node[-1][1]
        x2 = contour[-1][1] - 1
        y2 = contour[-1][0] - 1
        x3 = node[0][0]
        y3 = node[0][1]
        if not ((y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)):
            node.append((contour[-1][1] - 1, contour[-1][0] - 1))
        return node

    def _perimeters(self):
        for iter in range(len(self.contours)):
            nodes = self._nodes(self.contours[iter])
            a = 0
            b = 0
            nodes.append(nodes[0])
            for i in range(0, len(nodes) - 1):
                x1 = nodes[i][0]
                y1 = nodes[i][1]
                x2 = nodes[i + 1][0]
                y2 = nodes[i + 1][1]
                if x1 == x2:
                    a = abs(y1 - y2) + a
                elif y1 == y2:
                    a = abs(x1 - x2) + a
                else:
                    b = b + abs(y1 - y2)
            self.perimeters[iter] = (round(a * 0.4, 1), b)

    def _areas(self):
        for iter in range(len(self.contours)):
            nodes = self._nodes(self.contours[iter])
            a = 0
            nodes.append(nodes[0])
            for i in range(0, len(nodes) - 1):
                x1 = nodes[i][0] * 0.4
                y1 = nodes[i][1] * 0.4
                x2 = nodes[i + 1][0] * 0.4
                y2 = nodes[i + 1][1] * 0.4
                a = a + (x1 * y2 - x2 * y1)
            self.areas[iter] = a / 2

    def _convexes(self):
        for iter in range(len(self.contours)):
            nodes = self._nodes(self.contours[iter])
            nodes.append(nodes[0])
            flag = True
            for i in range(0, len(nodes) - 2):
                x1 = nodes[i][0]
                y1 = nodes[i][1]
                x2 = nodes[i + 1][0]
                y2 = nodes[i + 1][1]
                x3 = nodes[i + 2][0]
                y3 = nodes[i + 2][1]
                p1x = x2 - x1
                p1y = y2 - y1
                p2x = x3 - x2
                p2y = y3 - y2
                if (p1x * p2y - p2x * p1y) < 0:
                    self.convexes[iter] = False
                    flag = False
                    break
            if flag:
                self.convexes[iter] = True

    def _rotations(self):
        for x in range(len(self.contours)):
            contour = self.contours[x]
            self.rotations[x] = self._rotations_helper(contour)

    def _rotations_helper(self, contour):
        contour.append(contour[1])
        list = []
        for i in range(len(contour[:-2])):
            x1 = contour[i][0]
            y1 = contour[i][1]
            x2 = contour[i + 1][0]
            y2 = contour[i + 1][1]
            x3 = contour[i + 2][0]
            y3 = contour[i + 2][1]
            p1y = x1 - x2
            p1x = y1 - y2
            p2y = x3 - x2
            p2x = y3 - y2
            tt = round(math.acos((p1x * p2x + p1y * p2y) / (
                    ((p1x * p1x + p1y * p1y) ** 0.5) * ((p2x * p2x + p2y * p2y) ** 0.5))) * 180 / math.pi)
            if tt == 180:
                tt = 0
            list.append(tt)
        for i in range(1, len(list)):
            sli = list[:i]
            tmp_list = []
            for e in list:
                tmp_list.append(e)
            flag = True
            iter = 0
            while flag:
                for j in range(i):
                    if sli[j] == tmp_list[j]:
                        pass
                    else:
                        flag = False
                        iter = 0
                        break
                if flag:
                    iter = iter + 1
                    tmp_list = tmp_list[i:]
                    if len(tmp_list) < i:
                        if tmp_list == []:
                            return iter
                        else:
                            break
        return 1

    def _depths(self):
        contours1 = []
        for c in self.contours:
            tmp = []
            for n in c:
                tmp.append(n)
            contours1.append(tmp)
        self.depths = [-1 for _ in range(0, len(contours1))]
        for j in range(len(contours1)):
            flag = 0
            c = contours1[j]
            point = c[0]
            for i in range(len(contours1)):
                c1 = contours1[i]
                point1 = c1[0]
                if not (point1 == point):
                    if self._check(point, c1):
                        if self.depths[i] == -1:
                            pass
                        else:
                            self.depths[j] = self.depths[i] + 1
                            flag = 1
            if flag == 0:
                self.depths[j] = 0

    def analyse(self):
        for iter in range(len(self.contours)):
            (a, b) = self.perimeters[iter]
            area = self.areas[iter]
            convex = self.convexes[iter]
            output_strings = "Polygon " + str(iter + 1) + ":\n"
            if not (b == 0) and not (a == 0):
                output_strings += "    Perimeter: " + str(a) + str(" + ") + str(b) + str("*sqrt(.32)") + '\n'
            elif a == 0:
                output_strings += "    Perimeter: " + str(b) + str("*sqrt(.32)") + '\n'
            else:
                output_strings += "    Perimeter: " + str(a) + "\n"
            str_tmp = str(float('%.2f' % area))
            if str_tmp[-2] == ".":
                str_tmp = str_tmp + '0'
            output_strings += "    Area: " + str_tmp + "\n"
            if convex:
                output_strings += "    Convex: yes\n"
            else:
                output_strings += "    Convex: no\n"
            output_strings += "    Nb of invariant rotations: " + str(self.rotations[iter]) + '\n'
            output_strings += "    Depth: " + str(self.depths[iter])
            print(output_strings)

    def _check(self, pc, contour_tmp):
        x_pc = pc[0]
        y_pc = pc[1]
        UDLR = [0, 0, 0, 0]
        contour_tmp.append(contour_tmp[0])
        for p in contour_tmp:
            if UDLR == [1, 1, 1, 1]:
                return True
            else:
                x_p = p[0]
                y_p = p[1]
                if x_p == x_pc and y_p > y_pc:
                    UDLR[0] = 1
                elif x_p == x_pc and y_p < y_pc:
                    UDLR[1] = 1
                elif x_p > x_pc and y_p == y_pc:
                    UDLR[2] = 1
                elif x_p < x_pc and y_p == y_pc:
                    UDLR[3] = 1
        return False

    def display(self):
        file_object = open(self.name + ".tex", 'w')
        seq = []
        seq.append("\\documentclass[10pt]{article}\n")
        seq.append("\\usepackage{tikz}\n")
        seq.append("\\usepackage[margin=0cm]{geometry}\n")
        seq.append("\\pagestyle{empty}\n\n")
        seq.append("\\begin{document}\n\n")
        seq.append("\\vspace*{\\fill}\n")
        seq.append("\\begin{center}\n")
        seq.append("\\begin{tikzpicture}[x=0.4cm, y=-0.4cm, thick, brown]\n")

        output_strings = "\\draw[ultra thick] (0, 0) -- " + "(" + str(self.cs - 3) + ", " + "0" + ") -- " \
               + "(" + str(self.cs - 3) + ", " + str(self.rs - 3) + ") -- " \
               + "(" + "0" + ", " + str(self.rs - 3) + ") -- cycle;\n\n"

        seq.append(output_strings)
        max_depth = max(self.depths)
        for i in range(max_depth + 1):
            if i in self.depths:
                seq.append("% Depth " + str(i) + "\n")
                for j in range(len(self.contours)):
                    if self.depths[j] == i:
                        contour = self.contours[j]
                        nodes = self._nodes(contour)
                        seq.append(self._writePath(nodes, j))

        seq.append("\\end{tikzpicture}\n")
        seq.append("\\end{center}\n")
        seq.append("\\vspace*{\\fill}\n\n")
        seq.append("\\end{document}\n")
        file_object.writelines(seq)
        file_object.close()

    def _writePath(self, nodes, j):
        output_strings = ""
        max_area = max(self.areas)
        min_area = min(self.areas)
        area = self.areas[j]

        color = "orange!" + str(int(round(100 - (area - min_area) / (max_area - min_area) * 100))) + "!yellow"
        output_strings = output_strings + "\\filldraw[fill=" + color + "] "
        for i in range(len(nodes) - 1):
            n = nodes[i]
            output_strings = output_strings + "(" + str(n[0]) + ", " + str(n[1]) + ") -- "
        output_strings = output_strings + "cycle;\n"
        return output_strings

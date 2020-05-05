#!/usr/bin/python3
import pyeda.inter as pd
from itertools import combinations


class Error(Exception):
    def __init__(self, error_type):
        self.type = error_type


class ErrorMsg(Error):
    def __init__(self, error_type, msg):
        Error.__init__(self, error_type)
        self.msg = msg

    def print_msg(self):
        print(self.type, ' : ', self.msg)


class Grid:
    """
    Class for grid of cells.

    Attributes
    ----------
    rows: int
        number of rows
    columns: int
        number of columns
    colors: int
        number of colors
    """

    def __init__(self, rows, columns, colors):
        self.rows = rows
        self.columns = columns
        self.colors = colors
        # Create 3d array of boolean variables per each color/cell
        self.vars = pd.exprvars('x', rows, columns, colors)
        self.f_list = []

    def color_form(self, rule):
        """
        Generate constrant for cell's colour
        """
        self.f_list.append(self.vars[rule.c.y, rule.c.x, rule.color])

    def ncolor_form(self, rule):
        self.f_list.append(~self.vars[rule.c.y, rule.c.x, rule.color])

    def balanced_form(self, rule):
        self.f_list.append(pd.And(*[
            pd.And(*[self.in_rect_combinations(
                r, c, rule.c.y, rule.c.x, v,
                rule.c.x * rule.c.y // self.colors)
                for v in range(0, self.colors)])
            for r in range(0, self.rows - rule.c.y + 1)
            for c in range(0, self.columns - rule.c.x + 1)]))

    def nbalanced_form(self, rule):
        self.f_list.append(pd.And(*[
            pd.Or(*[~self.in_rect_combinations(
                r, c, rule.c.y, rule.c.x, v,
                rule.c.y * rule.c.x // self.colors)
                for v in range(0, self.colors)])
            for r in range(0, self.rows - rule.c.y + 1)
            for c in range(0, self.columns - rule.c.x + 1)])
        )

    def mixed_form(self, rule):
        self.f_list.append(pd.And(*[
            pd.And(*[
                pd.And(*[
                    pd.Or(*[~self.vars[
                        r + cell // rule.c.x, c + cell % rule.c.x, v]
                        for cell in range(0, rule.c.x * rule.c.y)])
                    for v in range(0, self.colors)])
                for c in range(0, self.columns - rule.c.x + 1)])
            for r in range(0, self.rows - rule.c.y + 1)]))

    def rich_form(self, rule):
        self.f_list.append(pd.And(*[
            pd.And(*[
                pd.And(*[
                    pd.Or(*[self.vars[
                        r + cell // rule.c.x, c + cell % rule.c.x, v]
                        for cell in range(0, rule.c.x * rule.c.y)])
                    for v in range(0, self.colors)])
                for c in range(0, self.columns - rule.c.x + 1)])
            for r in range(0, self.rows - rule.c.y + 1)]))

    def ebalanced_form(self, rule):
        self.f_list.append(pd.And(*[
            pd.And(*[self.in_figure_combinations(
                r, c, rule.vc, v, len(rule.vc) // self.colors)
                for r in range(0, self.rows - rule.c.y)
                for c in range(0, self.columns - rule.c.x)]
            )
            for v in range(0, self.colors)]))

    def enbalanced_form(self, rule):
        self.f_list.append(pd.And(*[
            pd.Or(*[~self.in_figure_combinations(
                r, c, rule.vc, v, len(rule.vc) // self.colors)
                for v in range(0, self.colors)]
            )
            for r in range(0, self.rows - rule.c.y)
            for c in range(0, self.columns - rule.c.x)])
        )

    def emixed_form(self, rule):
        self.f_list.append(pd.And(*[
            pd.And(*[
                pd.And(*[
                    pd.Or(*[~self.vars[r + cell.y, c + cell.x, v]
                            for cell in rule.vc])
                    for v in range(0, self.colors)])
                for c in range(0, self.columns - rule.c.x)])
            for r in range(0, self.rows - rule.c.y)]))

    def erich_form(self, rule):
        self.f_list.append(pd.And(*[
            pd.And(*[
                pd.And(*[
                    pd.Or(*[self.vars[r + cell.y, c + cell.x, v]
                            for cell in rule.vc])
                    for v in range(0, self.colors)])
                for c in range(0, self.columns - rule.c.x)])
            for r in range(0, self.rows - rule.c.y)]))

    def rules_to_formulas(self, c_list):
        for r in c_list:
            if r.type == RType.COLOR:
                self.color_form(r)
            elif r.type == RType.NCOLOR:
                self.ncolor_form(r)
            elif r.type == RType.BALANCED:
                self.balanced_form(r)
            elif r.type == RType.NBALANCED:
                self.nbalanced_form(r)
            elif r.type == RType.MIXED:
                self.mixed_form(r)
            elif r.type == RType.RICH:
                self.rich_form(r)
            elif r.type == RType.EBALANCED:
                self.ebalanced_form(r)
            elif r.type == RType.ENBALANCED:
                self.enbalanced_form(r)
            elif r.type == RType.EMIXED:
                self.emixed_form(r)
            elif r.type == RType.ERICH:
                self.erich_form(r)

    def get_val(self, point, r, c):
        for v in range(0, self.colors):
            if point[self.vars[r, c, v]]:
                return str(v)
        return "X"

    def display(self, point):
        chars = [[0] * self.columns for i in range(self.rows)]
        for r in range(0, self.rows):
            for c in range(0, self.columns):
                chars[r][c] = self.get_val(point, r, c)
        return chars

    def in_figure_combinations(self, r0, c0, coord_list, v, size):
        """
        Generates DNF from conjunction per every combination from
        cells in coord_list of specified size and colour

        :param r0: start row
        :param c0: start column
        :param coord_list: list of cells
        :param v: colour
        :param size: number of cells in subset
        """
        # coord_list.append(Coord(0, 0))
        # coord_list = list(set(coord_list))
        comb = combinations(coord_list, size)
        conj = []
        all_conj = []
        if size == 0:
            return pd.And(*[~self.vars[r0 + it.y, c0 + it.x, v]
                            for it in coord_list])
        for it in comb:
            for cell in coord_list:
                if cell in it:
                    conj.append(self.vars[r0 + cell.y, c0 + cell.x, v])
            all_conj.append(pd.And(*conj))
            conj = []
        return pd.Or(*all_conj)

    def in_rect_combinations(self, r0, c0, y, x, v, size):
        """
        Generates DNF from conjunction per every combination from
        cells in rectangle defined by top-left cell, length and heigh
        of specified size and colour

        :param r0: top row of a rectangle
        :param c0: the leftmost column of a rectangle
        :param y: height
        :param x: length
        :param v: colour
        :param size: size of rectangle
        """
        comb = combinations(range(0, y*x), size)
        conj = []
        all_conj = []
        if size == 0:
            return pd.And(*[~self.vars[r0+i, c0+j, v]
                            for i in range(0, y) for j in range(0, x)])
        for it in comb:
            for cell in range(0, x*y):
                if cell in it:
                    conj.append(self.vars[r0 + cell // x, c0 + cell % x, v])
            all_conj.append(pd.And(*conj))
            conj = []
        return pd.Or(*all_conj)

    def in_rows_combinations(self, r, v, size):
        comb = combinations(range(0, self.columns), size)
        conj = list()
        all_conj = list()
        if size == 0:
            return pd.And(*[~self.vars[r, c, v]
                            for c in range(0, self.columns)])
        for it in comb:
            for c in range(0, self.columns):
                if c in it:
                    conj.append(self.vars[r, c, v])
            all_conj.append(pd.And(*conj))
            conj = []
        return pd.Or(*all_conj)

    def in_cols_combinations(self, c, v, size):
        comb = combinations(range(0, self.rows), size)
        conj = list()
        all_conj = list()
        if size == 0:
            return pd.And(*[~self.vars[r, c, v] for r in range(0, self.rows)])
        for it in comb:
            for r in range(0, self.rows):
                if r in it:
                    conj.append(self.vars[r, c, v])
            all_conj.append(pd.And(*conj))
            conj = []
        return pd.Or(*all_conj)


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __hash__(self):
        return hash((self.x, self.y))


class Rule:
    def __init__(self, rtype=0, x=0, y=0, color=0):
        self.type = rtype
        self.c = Coord(x, y)
        self.vc = []
        self.color = color


def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


rule_type = {
    'bad': 0,
    'exit': 1,
    'solve': 2,
    'back': 3,
    'color': 4,
    'ncolor': 5
}


class RType:
    BAD, EXIT, SOLVE, BACK, COLOR, NCOLOR, BALANCED, NBALANCED, MIXED, RICH,\
        EBALANCED, ENBALANCED, EMIXED, ERICH = range(
            14)


class Commands:
    def __init__(self, rows, columns, colors):
        self.rows = rows
        self.columns = columns
        self.colors = colors
        self.c_list = []
        self.com = Rule()

    def check_type(self, rtype):
        if rtype == 'exit':
            return RType.EXIT
        elif rtype == 'solve':
            return RType.SOLVE
        elif rtype == 'back':
            return RType.BACK
        elif rtype == 'color':
            return RType.COLOR
        elif rtype == 'ncolor':
            return RType.NCOLOR
        elif rtype == 'balanced':
            return RType.BALANCED
        elif rtype == 'nbalanced':
            return RType.NBALANCED
        elif rtype == 'mixed':
            return RType.MIXED
        elif rtype == 'rich':
            return RType.RICH
        elif rtype == 'ebalanced':
            return RType.EBALANCED
        elif rtype == 'enbalanced':
            return RType.ENBALANCED
        elif rtype == 'emixed':
            return RType.EMIXED
        elif rtype == 'erich':
            return RType.ERICH
        else:
            return RType.BAD

    def check_arg(self, com):
        if (self.com.type == RType.EXIT) or (self.com.type == RType.SOLVE) or\
                (self.com.type == RType.BACK):
            if len(com) > 1:
                print('InvalidArguments : ',
                      com[0], 'does not have any arguments')
                return 1
        elif (self.com.type == RType.COLOR) or (self.com.type == RType.NCOLOR):
            if len(com) != 4:
                print('InvalidArguments : ', com[0], 'must have 3 arguments')
                return 1
            try:
                self.com.c.y = int(com[1])
                self.com.c.x = int(com[2])
                self.com.color = int(com[3])
            except ValueError:
                print('InvalidArguments : arguments must be integers')
                return 1
            if not (0 <= self.com.c.x < self.columns) or\
                    not (0 <= self.com.c.y < self.rows) or\
                    not (0 <= self.com.color < self.colors):
                print('InvalidArguments:\
                      x in [0, ', self.rows, '), y in [0, ',
                      self.columns, '), color in [0, ', self.colors, ')')
                return 1
        elif ((self.com.type == RType.BALANCED) or
              (self.com.type == RType.NBALANCED) or
              (self.com.type == RType.MIXED) or (self.com.type == RType.RICH)):
            if len(com) != 3:
                print('InvalidArguments : ', com[0], 'must have 2 arguments')
                return 1
            try:
                self.com.c.y = int(com[1])
                self.com.c.x = int(com[2])
            except ValueError:
                print('InvalidArguments : argument must be integers')
                return 1
            if not (0 < self.com.c.x <= self.columns) or\
                    not (0 < self.com.c.y <= self.rows):
                print('InvalidArguments : x in (0, ', self.rows,
                      '], y in (0, ', self.columns, ']')
                return 1
            if (not (self.com.c.x * self.com.c.y % self.colors == 0) and
                    not (self.com.type == RType.MIXED) and
                    not (self.com.type == RType.RICH)):
                print(
                    'InvalidValue:\
                     number of cells must divisible by number of colors')
                return 1
        elif ((self.com.type == RType.EBALANCED) or
              (self.com.type == RType.ENBALANCED) or
              (self.com.type == RType.EMIXED) or
              (self.com.type == RType.ERICH)):
            if ((len(com) - 1) % 2 != 0) or (len(com) < 3):
                print('InvalidArguments : ',
                      com[0], 'must have even number of arguments')
                return 1
            if (((len(com) + 1) % self.colors * 2 != 0) and not (
                    (self.com.type == RType.EMIXED) or
                    (self.com.type == RType.ERICH))):
                print(
                    'InvalidArguments:\
                    number of cells plus one\
                    must be divisible by number of colors')
                return 1
            try:
                for i in range(1, len(com), 2):
                    x = int(com[i + 1])
                    y = int(com[i])
                    if not (0 <= x < self.columns) or not (0 <= y < self.rows):
                        print(
                            'InvalidArguments:\
                             x in [0, ', self.rows, '),\
                             y in [0, ', self.columns, ')')
                        return 1
                    self.com.vc.append(Coord(x, y))
                    if self.com.c.x < x:
                        self.com.c.x = x
                    if self.com.c.y < y:
                        self.com.c.y = y
                self.com.vc.append(Coord(0, 0))
                self.com.vc = list(set(self.com.vc))
            except ValueError:
                print('InvalidArguments : arguments must be integers')
                return 1
        else:
            return 0

    def parse_str(self, string):
        lex = string.split(" ")
        self.com.type = self.check_type(lex[0])
        if self.com.type == RType.BAD:
            print('InvalidCommand : ', lex[0])
            return 1
        if self.check_arg(lex):
            return 1
        return 0

    def push_rule(self):
        self.c_list.append(self.com)
        self.com = Rule()

    def remove_last(self):
        if len(self.c_list) > 0:
            del self.c_list[-1]


class Solver:
    """
    Main class in unruly solver. It uses pyeda to transform
    grid of colored cells into boolean equation and solves it with
    PicoSAT solver

    Attributes
    ----------
    rows: int
        number of rows
    columns: int
        number of columns
    colors: int
        number of colors
    fixed_cells: list
        list of cells with fixed colors formatted
        as list of tuples: (row, column, color)

    Example
    -------

    >>Solver(6, 6, 3, [(0, 0, 2), (1, 3, 1)])
    """

    def __init__(self, rows, columns, colors, fixed_cells=[]):
        Solver._validate_args(rows, columns, colors, fixed_cells)
        self.rows = rows
        self.columns = columns
        self.colors = colors
        self.grid_inst = Grid(self.rows, self.columns, self.colors)
        self.commands = Commands(self.rows, self.columns, self.colors)
        for cell in fixed_cells:
            self.commands.c_list.append(
                Rule(RType.COLOR, cell[1], cell[0], cell[2]))

    def solve(self):
        """
        Seeks for solution for defined grid by means of PicoSAT
        """
        self.grid_inst.rules_to_formulas(self.commands.c_list)

        # Conjunction of all boolean variables representing the grid
        v_f = pd.And(*[
            pd.And(*[
                pd.OneHot(*[self.grid_inst.vars[r, c, v]
                            for v in range(0, self.colors)])
                for c in range(0, self.columns)])
            for r in range(0, self.rows)])

        r_diff = 3
        c_diff = 3

        # Conjunctions of disjunctions for every row demanding that there no
        # three consective cells with the same colour
        r_d_f = pd.And(*[
            pd.And(*[
                pd.And(*[
                    pd.Or(*[~self.grid_inst.vars[r, c, v]
                            for c in range(it, it + r_diff)])
                    for v in range(0, self.colors)])
                for it in range(0, self.columns - r_diff + 1)])
            for r in range(0, self.rows)])

        # Conjunctions of disjunctions for every column demanding that there no
        # three consective cells with the same colour
        c_d_f = pd.And(*[
            pd.And(*[
                pd.And(*[
                    pd.Or(*[~self.grid_inst.vars[r, c, v]
                            for r in range(it, it + c_diff)])
                    for v in range(0, self.colors)])
                for it in range(0, self.rows - c_diff + 1)])
            for c in range(0, self.columns)])

        # Conjunctions for every row demanding equal number of cells per colour
        row_eq = pd.And(*[
            pd.And(*[self.grid_inst.in_rows_combinations(
                r, v, self.grid_inst.columns // self.grid_inst.colors)
                for r in range(0, self.rows)])
            for v in range(0, self.colors)])

        # Conjunctions for every column demanding equal number
        # of cells per colour
        col_eq = pd.And(*[
            pd.And(*[self.grid_inst.in_cols_combinations(
                c, v, self.grid_inst.rows // self.grid_inst.colors)
                for c in range(0, self.columns)])
            for v in range(0, self.colors)])

        # Conjunction of stated above formulas + formulas from additional rules
        s_f = pd.And(v_f, r_d_f, c_d_f, row_eq, col_eq,
                     *self.grid_inst.f_list).tseitin()

        return self.grid_inst.display(s_f.satisfy_one())

    @staticmethod
    def _validate_args(rows, columns, colors, fixed_cells=[]):
        if not((rows >= 2) and (columns >= 2) and (colors >= 2)):
            raise ValueError(
                'InvalidValue: all arguments should be greater than 2')
        if not (rows % colors == 0) or not (columns % colors == 0):
            raise ValueError(
                'InvalidValue:\
                 both arguments must divisible by the number of colors')
        if not all(r in range(rows + 1) and c in range(columns + 1)
                   and v in range(colors + 1) for (r, c, v) in fixed_cells):
            raise ValueError('InvalidValue: all cells should be within grid')

    def _parse_arg(self, argv):
        """
        Function for parsing input.

        :param argv: input string
        """
        if len(argv) != 4:
            print('InvalidArgument : wrong number of arguments')
            return 1
        try:
            r = int(argv[1])
            c = int(argv[2])
            v = int(argv[3])
        except ValueError:
            print('InvalidType : arguments must be integers')
            return 1
        if not((r >= 2) and (c >= 2) and (v >= 2)):
            print('InvalidValue : some arguments are less than 2')
            return 1
        if not (r % v == 0) or not (c % v == 0):
            print('InvalidValue :\
                both arguments must divisible by number of colors')
            return 1
        return 0

    def main(self, argv):
        """
        Main function that parses input and executes solver

        Input format: python3 solver.py $rows $columns $colors
        Script executed in interactive mode.
        Possible commands:

            colors x y c -- cell x y should be coloured with colour c;
            ncolor x y c -- cell x y shouldn't be coloured with colour c;
            balanced r c -- every submatrix with dimensions rxc should have
                same number of cells per colour;
            nbalanced r c -- no submatrix with dimensions rxc should have
                same number of cells per colour;
            mixed r c -- every submatrix with dimensions rxc should have cells
                with at least two colors;
            rich r c -- every submatrix with dimensions rxc should have at
                least one cell per every colour;
            ebalanced x1 y1 ... xk yk -- every subset of cells that contains
                arbitrary cell x y and cells in row xi and yi should have
                same number of cells per colour;
            enbalanced x1 y1 ... xk yk -- same option as ebalanced but
                for nbalanced;
            emixed x1 y1 ... xk yk -- same option as ebalanced but for mixed;
            erich x1 y1 ... xk yk -- same option as ebalanced but for rich;
            back -- cancel last command.

        :param argv: input string
        """
        if self._parse_arg(argv):
            return
        self.rows = int(argv[1])
        self.columns = int(argv[2])
        self.colors = int(argv[3])
        self.grid_inst = Grid(self.rows, self.columns, self.colors)
        self.commands = Commands(self.rows, self.columns, self.colors)
        # Interactive loop for additional commands
        while True:
            line = input("Enter command: ")
            if not self.commands.parse_str(line):
                if self.commands.com.type == RType.EXIT:
                    return
                elif self.commands.com.type == RType.BACK:
                    self.commands.remove_last()
                elif self.commands.com.type == RType.SOLVE:
                    self.grid_inst.rules_to_formulas(self.commands.c_list)
                    break
                else:
                    self.commands.push_rule()
        # Conjunction of all boolean variables representing the grid
        v_f = pd.And(*[
            pd.And(*[
                pd.OneHot(*[self.grid_inst.vars[r, c, v]
                            for v in range(0, self.colors)])
                for c in range(0, self.columns)])
            for r in range(0, self.rows)])

        r_diff = 3
        c_diff = 3

        # Conjunctions of disjunctions for every row demanding that there no
        # three consective cells with the same colour
        r_d_f = pd.And(*[
            pd.And(*[
                pd.And(*[
                    pd.Or(*[~self.grid_inst.vars[r, c, v]
                            for c in range(it, it + r_diff)])
                    for v in range(0, self.colors)])
                for it in range(0, self.columns - r_diff + 1)])
            for r in range(0, self.rows)])

        # Conjunctions of disjunctions for every column demanding that there no
        # three consective cells with the same colour
        c_d_f = pd.And(*[
            pd.And(*[
                pd.And(*[
                    pd.Or(*[~self.grid_inst.vars[r, c, v]
                            for r in range(it, it + c_diff)])
                    for v in range(0, self.colors)])
                for it in range(0, self.rows - c_diff + 1)])
            for c in range(0, self.columns)])

        # Conjunctions for every row demanding equal number of cells per colour
        row_eq = pd.And(*[
            pd.And(*[self.grid_inst.in_rows_combinations(
                r, v, self.grid_inst.columns //
                self.grid_inst.colors) for r in range(0, self.rows)])
            for v in range(0, self.colors)])

        # Conjunctions for every column demanding equal\
        # number of cells per colour
        col_eq = pd.And(*[
            pd.And(*[self.grid_inst.in_cols_combinations(
                c, v, self.grid_inst.rows // self.grid_inst.colors)
                for c in range(0, self.columns)])
            for v in range(0, self.colors)])

        # Conjunction of stated above formulas + formulas from additional rules
        s_f = pd.And(v_f, r_d_f, c_d_f, row_eq, col_eq,
                     *self.grid_inst.f_list).tseitin()
        try:
            self.grid_inst.display(s_f.satisfy_one())
        except TypeError:
            print(
                'It seems that there is no solution \
                to this puzzle with such constraints.')


# print(Solver(8, 6, 2, [(0, 0, 1)]).solve())

import random


def pytest_addoption(parser):
    """
    Process arguments to run tests with specified options.
    """
    parser.addoption("--rows", action="store", type=int, default=8,
                     help="Fix number of rows in generated board.")
    parser.addoption("--columns", action="store", type=int, default=8,
                     help="Fix number of columns in generated board.")
    parser.addoption("--colors", action="store", type=int, default=2,
                     help="Fix number of colors in generated board.")
    parser.addoption("--spec", action="store_true", default=False,
                     help="Run tests with special generator. \
                         Warning! This generator is for development of \
                             starting grid only and supposed to fail \
                                 few tests")
    parser.addoption("--runs", action="store", type=int, default=3,
                     help="Number of runs for each generator")


def pytest_generate_tests(metafunc):
    """
    Random tests generator for Unruly Solver.
    """
    if "params" in metafunc.fixturenames:
        n = metafunc.config.getoption("rows")
        m = metafunc.config.getoption("columns")
        c = metafunc.config.getoption("colors")
        r = metafunc.config.getoption("runs")
        params = ()

        for i in range(r):
            list_for_solver = _Rule2(n, m, c)
            params += (True, n, m, c, list_for_solver),
            if (metafunc.config.getoption("spec")):
                list_for_solver = _Rule1(n, m, c)
                params += (True, n, m, c, list_for_solver),

        metafunc.parametrize("params", params)


def _Rule1(n, m, c):
    result = list()
    row_c = [[2 * n // c // 3 for i in range(c)] for j in range(n)]
    col_c = [[2 * m // c // 3 for i in range(c)] for j in range(m)]
    n += 4
    m += 4
    board = [[-1 for j in range(m)] for i in range(n)]

    for i in range(2, n - 2):
        for j in range(2, m - 2):
            if random.randint(0, 1):
                poss = set()
                for a in range(-2, 3):
                    for b in range(-2, 3):
                        if (abs(a * b) == 1 or a * b == 0) and \
                                board[i + a][j + b] != -1:
                            poss = poss | {board[i + a][j + b]}
                if len(poss) == 0:
                    for color in range(c):
                        if row_c[i - 2][color] > 0 and col_c[j - 2][color] > 0:
                            poss = poss | {color}
                    if len(poss):
                        board[i][j] = random.choice(tuple(poss))
                        row_c[i - 2][board[i][j]] -= 1
                        col_c[j - 2][board[i][j]] -= 1
                        result.append((i - 2, j - 2, board[i][j]))
                    continue
                if len(poss) >= 2:
                    continue
                color = random.choice(tuple(poss))
                if row_c[i - 2][color] > 0 and col_c[j - 2][color] > 0:
                    poss = poss - ({board[i - 2][j]} & {board[i - 1][j]}) - \
                           ({board[i - 1][j]} & {board[i + 1][j]}) - \
                           ({board[i + 1][j]} & {board[i + 2][j]}) - \
                           ({board[i][j - 2]} & {board[i][j - 1]}) - \
                           ({board[i][j - 1]} & {board[i][j + 1]}) - \
                           ({board[i][j + 1]} & {board[i][j + 2]})
                    if len(poss) == 0:
                        continue
                    else:
                        board[i][j] = color
                        row_c[i - 2][board[i][j]] -= 1
                        col_c[j - 2][board[i][j]] -= 1
                        result.append((i - 2, j - 2, board[i][j]))
    return result


def _Rule2(n, m, c):
    result = list()
    for i in range(n):
        for j in range(m):
            if not random.randint(0, 7):
                result.append((i, j, (i % c + j % c) % c))
    return result

import random


def pytest_addoption(parser):
    parser.addoption("--rows", action="store", default="8",
                     help="set number of rows in generated board")
    parser.addoption("--columns", action="store", default="8",
                     help="set number of columns in generated board")
    parser.addoption("--colors", action="store", default="2",
                     help="set number of colors in generated board")
    parser.addoption("--all", action="store_true", default=False,
                     help="run tests for all generators")
    parser.addoption("--runs", action="store", default="1",
                     help="number of runs for each generator")
    parser.addoption("--rules", action="store", default="00",
                     help="choose active rules for generator \
                     in form of binary string")


def pytest_generate_tests(metafunc):
    if "params" in metafunc.fixturenames:
        n = eval(metafunc.config.getoption("rows"))
        m = eval(metafunc.config.getoption("columns"))
        c = eval(metafunc.config.getoption("colors"))
        r = eval(metafunc.config.getoption("runs"))
        params = ()
        if metafunc.config.getoption("all"):
            active_rules = "11"
        else:
            active_rules = metafunc.config.getoption("rules")

        for i in range(r):
            if active_rules[0] == '1':
                list_for_solver = _Rule1(n, m, c)
                params += (m, n, c, list_for_solver),
            if active_rules[1] == '1':
                list_for_solver = _Rule2(n, m, c)
                params += (m, n, c, list_for_solver),

        metafunc.parametrize("params", params)


def _Rule1(n, m, c):
    result = list()
    row_c = [[n / c for i in range(c)] for j in range(n)]
    col_c = [[m / c for i in range(c)] for j in range(m)]
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
                                board[i+a][j+b] != -1:
                            poss = poss | {board[i+a][j+b]}
                if len(poss) == 0:
                    for color in range(c):
                        if row_c[i - 2][color] > 0 and col_c[j - 2][color] > 0:
                            poss = poss | {color}
                    board[i][j] = random.choice(tuple(poss))
                    row_c[i - 2][board[i][j]] -= 1
                    col_c[j - 2][board[i][j]] -= 1
                    result.append((i - 2, j - 2, board[i][j]))
                if len(poss) >= 2:
                    continue
                color = random.choice(tuple(poss))
                if row_c[i - 2][color] > 0 and col_c[j - 2][color] > 0:
                    poss = poss - ({board[i-2][j]} & {board[i-1][j]}) - \
                        ({board[i-1][j]} & {board[i+1][j]}) - \
                        ({board[i+1][j]} & {board[i+2][j]}) - \
                        ({board[i][j-2]} & {board[i][j-1]}) - \
                        ({board[i][j-1]} & {board[i][j+1]}) - \
                        ({board[i][j+1]} & {board[i][j+2]})
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
    board = [[(i % c + j % c) % c for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if not random.randint(0, 2):
                result.append((i, j, board[i][j]))
    return result

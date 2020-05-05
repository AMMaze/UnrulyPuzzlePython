

def CheckSolution(board, rows, columns, colors):
    """
    Check if board meets requirements specified in the rules.

    :param board: list of all board cells formatted
        as list of tuples (row, column, color)
    :param rows: number of rows
    :param columns: number of comlumns
    :param colors: number of colors

    :Example:

        >>CheckSolution([[0, 0, 1, 1], [0, 0, 1, 1],
                         [1, 1, 0, 0], [1, 1, 0, 0]]
                         4, 4, 2)
    """
    for i in range(rows):
        colorCount = [0 for c in range(colors)]
        for j in range(columns):
            colorCount[board[i][j]] += 1
            if j >= 2 \
                and board[i][j] == board[i][j - 1] \
                    and board[i][j] == board[i][j - 2]:
                print(1)
                return False
        for j in range(colors):
            if colorCount[j] != columns / colors:
                print(2)
                return False

    for j in range(columns):
        colorCount = [0 for c in range(colors)]
        for i in range(rows):
            colorCount[board[i][j]] += 1
            if i >= 2 \
                and board[i][j] == board[i - 1][j] \
                    and board[i][j] == board[i - 2][j]:
                return False
        for i in range(colors):
            if colorCount[i] != rows / colors:
                return False
    return True

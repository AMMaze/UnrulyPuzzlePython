import pytest
from UnrulyPuzzlePython.solver.unruly_solver import Solver
from UnrulyPuzzlePython.solver.check_solution import CheckSolution


class TestClass_Solver:
    def test_Solver_gen(self, params):
        if params[0]:
            solution = Solver(*params[1:]).solve()
            for i in range(params[1]):
                for j in range(params[2]):
                    solution[i][j] = int(solution[i][j])
            assert CheckSolution(solution, *params[1:4])
        else:
            pytest.raises(TypeError, Solver(*params[1:]).solve)

    def test_Solver_sol(self):
        params = list()

        lst_for_solver = [(0, 0, 2)]
        params.append((6, 6, 3, lst_for_solver))

        lst_for_solver = [(0, 0, 1), (3, 0, 0),
                          (4, 2, 0), (5, 2, 0),
                          (1, 3, 0), (2, 3, 0),
                          (0, 4, 1), (4, 4, 0),
                          (7, 4, 0), (4, 5, 1),
                          (5, 5, 1), (7, 6, 0),
                          (4, 7, 1), (6, 7, 1)]
        params.append((8, 8, 2, lst_for_solver))

        lst_for_solver = [(0, 0, 2), (0, 3, 1),
                          (2, 1, 1), (3, 4, 0),
                          (3, 5, 1), (3, 7, 2),
                          (5, 1, 3), (5, 2, 2),
                          (7, 4, 2), (7, 7, 1)]
        params.append((8, 8, 4, lst_for_solver))

        for p in params:
            solution = Solver(*p).solve()
            for i in range(p[0]):
                for j in range(p[1]):
                    solution[i][j] = int(solution[i][j])
            assert CheckSolution(solution, *p[:3])

    def test_Solver_nsol(self):
        params = list()

        lst_for_solver = [(0, 0, 1), (0, 2, 1),
                          (1, 0, 1), (1, 1, 1),
                          (2, 1, 1), (2, 2, 1)]
        params.append((4, 4, 2, lst_for_solver))

        lst_for_solver = [(2, 0, 0), (2, 1, 0),
                          (3, 2, 1), (4, 2, 1),
                          (2, 3, 2), (2, 4, 2),
                          (0, 2, 3), (1, 2, 3)]
        params.append((8, 8, 4, lst_for_solver))

        lst_for_solver = [(0, 0, 0), (0, 1, 0),
                          (0, 2, 1), (0, 3, 0),
                          (0, 4, 0), (0, 5, 2)]
        params.append((6, 6, 3, lst_for_solver))

        for p in params:
            pytest.raises(TypeError, Solver(*p).solve)

    def test_Solver_validate_args(self):
        params = list()
        params.append((1, 10, 2, [0, 0, 0]))
        params.append((8, 6, 4, []))
        params.append((8, 10, 5, []))

        lst_for_solver = [(0, 0, 1), (2, 1, 0),
                          (4, 6, 3), (4, 7, 3),
                          (20, 1, 0)]
        params.append((8, 8, 4, lst_for_solver))
        for p in params:
            with pytest.raises(ValueError):
                Solver._validate_args(*p)

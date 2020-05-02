from solver.unruly_solver import Solver


class TestClass_Solver:
    def test_Solver_gen(self, params):
        assert Solver(*params).solve()

    def test_Solver_simple(self):
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

        for p in params:
            assert Solver(*p).solve()

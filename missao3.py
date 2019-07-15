#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Missão3: Implementar um algoritmo para mover um robô do canto
superior esquerdo para o canto inferior direito de uma grade.
"""

import unittest


def find_path(matrix):
    if not isinstance(matrix, (list, tuple)) or not len(matrix[0]):
        return None

    border = [0] * (len(matrix[0]) + 2)
    init, final = (1, 1), (len(matrix), len(matrix[0]))
    matrix = [border, *[[0] + i + [0] for i in matrix], border]
    change = True
    while change:
        change = False
        for x, row in enumerate(matrix[1:-1], 1):
            for y, col in enumerate(row[1:-1], 1):
                up = matrix[x - 1][y] + row[y - 1]
                down = matrix[x + 1][y] + row[y + 1]
                if col and (init != (x, y) != final) and (up == 0 or down == 0):
                    matrix[x][y] = 0
                    change = True

    coo, path = 0, []
    matrix2 = [i[1:-1] for i in matrix[1:-1]]
    for x, row in enumerate(matrix2):
        for y, col in enumerate(row):
            if col and x + y == coo:
                path.append((x, y))
                coo += 1
    if path == [(0, 0)]:
        return None
    return path


class TestGridPath(unittest.TestCase):

    def test_grid_path(self):
        self.assertIsNone(eval('find_path(None)'))
        self.assertIsNone(find_path([[]]))
        result = find_path([[1, 1, 1, 1],
                            [1, 0, 1, 1],
                            [1, 1, 0, 1],
                            [0, 1, 1, 1],
                            [1, 1, 0, 1],
                            [1, 1, 1, 0],
                            [1, 0, 1, 0],
                            [1, 0, 1, 1]])
        expected = [(0, 0), (1, 0), (2, 0),
                    (2, 1), (3, 1), (4, 1),
                    (5, 1), (5, 2), (6, 2),
                    (7, 2), (7, 3)]
        self.assertEqual(result, expected)
        self.assertIsNone(find_path([[1, 1, 0, 1],
                                     [1, 0, 1, 1]]))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Missão4: Implementar o Algoritmo de Ordenação "Selection sort".
"""

import unittest


def selection_sort(data):
    if not isinstance(data, (list, tuple)):
        raise TypeError

    for x1, n1 in enumerate(data):
        tmp = (x1, n1)
        for x2, n2 in enumerate(data[x1:], x1):
            if n2 <= tmp[1]:
                tmp = (x2, n2)
        data[x1], data[tmp[0]] = tmp[1], n1
    return data


class TestSelectionSort(unittest.TestCase):

    def test_selection_sort(self):
        self.assertRaises(TypeError, selection_sort, None)
        self.assertEqual(selection_sort([]), [])
        self.assertEqual(selection_sort([5]), [5])
        data = [5, 1, 7, 2, 6, -3, 5, 7, -10]
        self.assertEqual(selection_sort(data), sorted(data))


if __name__ == '__main__':
    unittest.main()

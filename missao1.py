#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Missão1: Implementar um algoritmo para determinar
se uma stringpossui todos os caracteres exclusivos.
"""

import unittest


def has_unique_chars(string):
    if not isinstance(string, str):
        return False
    for char in str(string):
        if string.count(char) > 1:
            return False
    return True


class TestUniqueChars(unittest.TestCase):

    def test_unique_chars(self):
        self.assertFalse(eval('has_unique_chars(None)'))
        self.assertTrue(has_unique_chars(''))
        self.assertFalse(has_unique_chars('foo'))
        self.assertTrue(has_unique_chars('bar'))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Missão2: Gerar uma lista de números primos.
"""

import unittest


def generate_primes(max_num):
    assert isinstance(max_num, int)

    prime = []
    for num in range(2, max_num + 1):
        for n in prime:
            if num % n == 0:
                break
        else:
            prime.append(num)
    return prime


class TestMath(unittest.TestCase):

    def test_generate_primes(self):
        self.assertRaises(AssertionError, generate_primes, None)
        self.assertRaises(AssertionError, generate_primes, 98.6)
        self.assertEqual(generate_primes(120), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                                                37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
                                                79, 83, 89, 97, 101, 103, 107, 109, 113])


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
"""
Assignment: The objective of this assignment is for you to (a) develop a set of tests for an 
existing triangle classification program, (b) use those tests to find and fix defects in that program, 
and (c) report on your testing results for the Triangle problem
@author: NehharShah
@author: Nihar Shah
Date: 20 September 2022
"""
import unittest
from triangle import classifyTriangle
# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework
class TestTriangle(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def test_invalid_sum_sides_a(self):
        self.assertEqual(classifyTriangle(10, 7, 2), 'Scalene', '10,7,2 is not a triangle')

    def test_invalid_sum_sides_b(self):
        self.assertEqual(classifyTriangle(7, 10, 2), 'Scalene', '7,10,2 is not a triangle')

    def test_valid_equilateral_triangle(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def test_valid_right_triangle_a(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def test_valid_right_triangle_b(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def test_valid_scalene_triangle_a(self):
        self.assertEqual(classifyTriangle(4, 6, 9), 'Scalene', '4,6,9 is a Scalene triangle')

    def test_valid_scalene_triangle_b(self):
        self.assertEqual(classifyTriangle(9, 4, 6), 'Scalene', '9,4,6 is a Scalene triangle')

    def test_valid_isosceles_triangle_a(self):
        self.assertEqual(classifyTriangle(3, 2, 2), 'Isosceles', '3,2,2 is a Isosceles triangle')

    def test_valid_isosceles_triangle_b(self):
        self.assertEqual(classifyTriangle(2, 3, 2), 'Isosceles', '2,3,2 is a Isosceles triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
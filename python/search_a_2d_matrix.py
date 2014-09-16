# coding=utf-8
# AC Rate: 31.2%
# SOURCE URL: https://oj.leetcode.com/problems/search-a-2d-matrix/
#
# Write an efficient algorithm that searches for a value in an m x n matrix. Th
# is matrix has the following properties:
#
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previou
# s row.
#
#
#
# For example,
#
# Consider the following matrix:
#
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
#
# Given target = 3, return true.
#


class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        
# coding=utf-8
# AC Rate: 21.4%
# https://oj.leetcode.com/problems/largest-rectangle-in-histogram/

# Given n non-negative integers representing the histogram's bar height where the
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
# For example,
# Given height = [2,1,5,6,2,3],
# return 10.

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        
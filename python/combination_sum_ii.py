# coding=utf-8
# AC Rate: 24.6%
# https://oj.leetcode.com/problems/combination-sum-ii/

# Given a collection of candidate numbers (C) and a target number (T), find all
# Each number in C may only be used once in the combination.
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order.
# The solution set must not contain duplicate combinations.
# For example, given candidate set 10,1,2,7,6,1,5 and target 8,
# A solution set is:
# [1, 7]
# [1, 2, 5]
# [2, 6]
# [1, 1, 6]

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        
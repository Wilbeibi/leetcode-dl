# coding=utf-8
# AC Rate: 11.4%
# https://oj.leetcode.com/problems/word-ladder-ii/

# Given two words (start and end), and a dictionary, find all shortest
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# For example,
# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
# Note:
# All words have the same length.
# All words contain only lowercase alphabetic characters.

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        
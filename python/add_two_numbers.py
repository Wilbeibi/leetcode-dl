# coding=utf-8
# AC Rate: 23.0%
# https://oj.leetcode.com/problems/add-two-numbers/

# You are given two linked lists representing two non-negative numbers. The
# digits are stored in reverse order and each of their nodes contain a single
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        
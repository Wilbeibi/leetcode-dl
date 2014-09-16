# coding=utf-8
# AC Rate: 35.4%
# SOURCE URL: https://oj.leetcode.com/problems/populating-next-right-pointers-i
# n-each-node/
#
#
# Given a binary tree
#
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
#
#
# Populate each next pointer to point to its next right node. If there is no ne
# xt right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.
#
# Note:
#
# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the sa
# me level, and every parent has two children).
#
#
#
# For example,
# Given the following perfect binary tree,
#
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
#
#
#
# After calling your function, the tree should look like:
#
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL
#
#
#


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        
# coding=utf-8
# AC Rate: 23.7%
# https://oj.leetcode.com/problems/recover-binary-search-tree/

# Two elements of a binary search tree (BST) are swapped by mistake.
# Recover the tree without changing its structure.
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized
# OJ's Binary Tree Serialization:
# The serialization of a binary tree follows a level order traversal, where '#'
# Here's an example:
#    1
#   / \
#  2   3
#     /
#    4
#     \
#      5
# The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        
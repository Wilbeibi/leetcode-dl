// coding=utf-8
// AC Rate: 27.3%
// https://oj.leetcode.com/problems/unique-binary-search-trees-ii/

// Given n, generate all structurally unique BST's (binary search trees) that
// For example,
// Given n = 3, your program should return all 5 unique BST's shown below.
//    1         3     3      2      1
//     \       /     /      / \      \
//      3     2     1      1   3      2
//     /     /       \                 \
//    2     1         2                 3
// confused what "{1,#,2,3}" means? > read more on how binary tree is serialized
// OJ's Binary Tree Serialization:
// The serialization of a binary tree follows a level order traversal, where '#'
// Here's an example:
//    1
//   / \
//  2   3
//     /
//    4
//     \
//      5
// The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".

/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<TreeNode *> generateTrees(int n) {
        
    }
};
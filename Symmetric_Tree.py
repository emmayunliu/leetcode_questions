# https://leetcode.com/problems/symmetric-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)
        

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            inner = self.isMirror(left.right, right.left)
            outer = self.isMirror(left.left, right.right)
            return inner and outer
        else:
            return False

class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        mid = int(len(nums)/2)-1
        root = TreeNode(nums[mid])
        left = nums[:mid]
        right = nums[mid + 1:]
        while mid >= 0:
            root.left = mid - 1
            root.right = len(nums) - 1



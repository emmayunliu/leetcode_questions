https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

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
        if not nums:
            return None
        mid = i//2
        root = TreeNode(nums[mid])
        root.left = sortedArrayToBST(nums[:mid])
        root.right = sortedArrayToBST(nums[mid+1:])
        return root
        
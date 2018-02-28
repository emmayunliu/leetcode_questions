# https://leetcode.com/problems/contains-duplicate/description/
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for int in nums:
            if int in dic:
                return True
            else:
                dic[int] = 1
        return False

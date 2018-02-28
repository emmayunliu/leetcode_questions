# https://leetcode.com/problems/missing-number/description/
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(0, max(nums)+2):
        #     if i not in nums:
        #         return i
        n = len(nums)
        return n*(n+1)/2 - sum(nums)
obj = Solution()
print obj.missingNumber([])
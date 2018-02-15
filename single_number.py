# https://leetcode.com/problems/single-number/description/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        storage = {}
        for item in nums:
            if item in storage:
                del storage[item]
            else:
                storage[item] = 1
        return storage.keys()[0]

obj = Solution()
print obj.singleNumber([1,2,3,4,1,2,3])

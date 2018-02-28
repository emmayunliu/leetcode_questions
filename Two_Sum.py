# https://leetcode.com/problems/two-sum/description/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for index, i in enumerate(nums):
        #     if target-i in nums[index+1:]:
        #         return [index, nums[index+1:].index(target-i)+index+1]
        dic = {}
        for index, num in enumerate(nums):
            if num in dic:
                return [dic[num], index]
            else:
                dic[target-num] = index


obj = Solution()
print obj.twoSum([3,2,4], 6)
# https://leetcode.com/problems/house-robber/description/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            temp = last
            last = now
            now = max(temp+i, now)
        return now

obj = Solution()
print obj.rob([2,1,5,1,1,7,9,10])
# f(0) = nums[0]
# f(1) = max(nums[0], nums[1])
# f(2) = max(nums[0]+nums[2], nums[1]) 
# f(3) = max(nums[0]+nums[2], nums[1]+nums[3], nums[0]+nums[3])
# f(k) = max(f(k-1), f(k-2)+nums(k))



class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        length = len(nums)
        for i in range(length + 1):
            if 0 not in nums:
                nums = nums.extend([0] * count)
                return nums
            else:
                nums.remove(0)
                count += 1


nums = [0, 1, 0, 3, 12]
obj = Solution()
print obj.moveZeroes(nums)

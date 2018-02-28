# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        compare = 0
        for index in range(1, len(nums)):
            if nums[index] != nums[index-1]:
                compare += 1
        return compare + 1
            

obj = Solution()
print obj.removeDuplicates([1,1,1,1,1,1,2,2,2,2])

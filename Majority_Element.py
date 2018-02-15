class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return None
        storage = {}
        for char in nums:
            if char in storage:
                storage[char] += 1
                if storage[char] > len(nums)/2:
                    return char
            else:
                storage[char] = 1
        return None

obj = Solution()
print obj.majorityElement([1,1,1,1,2,2])

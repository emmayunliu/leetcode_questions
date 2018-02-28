class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums, n):
        self.count = 0
        if not nums:
            return -1
        self.kth(nums, 0, len(nums) - 1, n)
        print self.count
        return self.count

    def kth(self, nums, left, right, k):
        # if left >= right: return nums[right]
        m = left
        for i in xrange(left + 1, right + 1):
            self.count += 1
            if nums[i] < nums[left]:
                m += 1
                nums[m], nums[i] = nums[i], nums[m]

        # swap between m and l after partition, important!
        nums[m], nums[left] = nums[left], nums[m]

        if m + 1 == k:
            return nums[m]
        elif m + 1 > k:
            return self.kth(nums, left, m - 1, k)
        else:
            return self.kth(nums, m + 1, right, k)

obj = Solution()
nums = [20,21,22,23,18,19,4,5,3,2,1,9,8,7,6,24,25,11,12,13,14,15,16,17,10]
sum = 0
for n in range(1, 26):
    sum += obj.median(nums, n)

print sum

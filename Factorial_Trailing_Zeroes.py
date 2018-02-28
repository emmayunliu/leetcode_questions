# https://leetcode.com/problems/factorial-trailing-zeroes/description/

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count, i = 0, 5
        while n/i >= 1:
            count += n/i
            i *= 5
        return int(count)



obj = Solution()
print obj.trailingZeroes(5)

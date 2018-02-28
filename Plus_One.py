# https://leetcode.com/problems/plus-one/description/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = 0
        length = len(digits)
        for index, integer in enumerate(digits):
            sum += integer * (10 ** (length-index-1))
        return [i for i in str(sum+1)]

obj = Solution()
print obj.plusOne([9,9])
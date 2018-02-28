# https://leetcode.com/problems/number-of-1-bits/description/

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)
        index = binary.index('b')
        count = 0
        for char in binary[index+1:]:
            if char == '1':
                count += 1
        return count

obj = Solution()
obj.hammingWeight(11)
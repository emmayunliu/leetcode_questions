# https://leetcode.com/problems/power-of-three/description/

import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 3:
            return False
        x = math.log(n, 3)
        return abs(round(x) - x) < 0.0000000000001

obj = Solution()
print obj.isPowerOfThree(27)
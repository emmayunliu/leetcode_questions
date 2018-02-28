# https://leetcode.com/problems/climbing-stairs/description/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        if n == 1:
            return 1
        res = [0 for i in xrange(n)]
        res[0], res[1] = 1, 2
        for i in xrange(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]
            
obj = Solution()
print obj.climbStairs(5)

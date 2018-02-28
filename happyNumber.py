# https://leetcode.com/problems/happy-number/description/

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # base case: square sum inclues only 1 and 0
        mem = set()
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True

obj = Solution()
print obj.isHappy(20)
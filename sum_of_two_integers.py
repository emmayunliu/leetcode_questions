# https://leetcode.com/problems/sum-of-two-integers/description/
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        self.list = []
        if a >= 0 and b >= 0:
            self.add(a)
            self.add(b)
            return len(self.list)
        elif a <= 0 and b <= 0:
            self.add(-a)
            self.add(-b)
            return -len(self.list)
        elif a >= 0 and b <= 0:
            self.add(a)
            rest = self.remove(b)
            if rest == 0:
                return len(self.list)
            else:
                self.add(rest)
                return -len(self.list)
        else:
            self.add(b)
            rest = self.remove(a)
            if rest == 0:
                return len(self.list)
            else:
                self.add(rest)
                return -len(self.list)
    
    
    def add(self, n):
        for i in range(n):
            self.list.append(0)

    def remove(self, n):
        for i in range(-n):
            if len(self.list) <= 0:
                return -n - i
            else:
                self.list.pop()
        return 0

obj = Solution()
print obj.getSum(2147483647, -2147483648)

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,	'M': 1000}
        result = 0
        for index in range(len(s)-1):
            if romans[s[index]] >= romans[s[index+1]]:
                result += romans[s[index]]
            else:
                result -= romans[s[index]]
        result += romans[s[-1]]
        return result
obj = Solution()
print obj.romanToInt('IX')
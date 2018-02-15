# https://leetcode.com/problems/excel-sheet-column-number/description/
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        count = 0
        letters = ['A','B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for i in range(len(s)-1, -1, -1):
            count += 1
            if count == 1:
                result += letters.index(s[i]) + 1
            else:
                result += (letters.index(s[i]) + 1) * (26 ** (count-1))
        return result
        
        
       
obj = Solution()
print obj.titleToNumber('AA')
# https://leetcode.com/problems/valid-parentheses/description/


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {')': '(',
               '}': '{',
               ']': '['
        }
        stack = []
        for char in s:
            if char in dic.values():
                stack.append(char)
            elif char in dic.keys():
                if stack == [] or dic[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

obj = Solution()
print obj.isValid("()")
                
                

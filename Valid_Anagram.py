# https://leetcode.com/problems/valid-anagram/description/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # solution 1
        # return sorted(s) == sorted(t)
        # solution 2
        dic = {}
        for char in t:
            dic[char] = dic[char] + 1 if char in dic else 1
        for char in s:
            if char in dic:
                dic[char] -= 1
            else:
                return False
        for val in dic.values():
            if val != 0:
                return False
        return True

obj = Solution()
print obj.isAnagram("anagram", "nagaram")

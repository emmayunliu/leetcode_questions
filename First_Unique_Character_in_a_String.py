# https://leetcode.com/problems/first-unique-character-in-a-string/description/
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        storage = {}
        chars = []
        for index, char in enumerate(s):
            if char in storage:
                if char in chars:
                    chars.remove(char)
            else:
                storage[char] = index
                chars.append(char)

        return storage[chars[0]] if len(chars) > 0 else -1
        
obj = Solution()
print obj.firstUniqChar('loveleetcode')


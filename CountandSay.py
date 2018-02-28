# https://leetcode.com/problems/count-and-say/description/


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # f(k) = 
        # for index, num in f(k-1):
        #  if num == f(k-1)[index+1]
        # count++
        # else f(k) += 'count' + 'num
        if n == 1:
            return 1
        if n == 2:
            return 22
        result = '11' 
        for i in range(n-2):
            newResult = ''
            count = 1
            for index in range(len(result)-1):
                if result[index] == result[index+1]:
                    count += 1
                else:
                    newResult += `count` + result[index]
                    count = 1
                if index == len(result)-2:
                    newResult += `count` + result[index+1]
            result = newResult
                    
        return result
obj = Solution()
print obj.countAndSay(6)
                    
        
            
            

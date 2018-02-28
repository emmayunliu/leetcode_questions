# https://leetcode.com/problems/fizz-buzz/description/
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # if n < 1:
        #     return None
        # result = []
        # for i in range(1, n+1):
        #     if i % 3 == 0 and i % 5 == 0:
        #         result.append('FizzBuzz')
        #     elif i % 3 == 0:
        #         result.append('Fizz')
        #     elif i % 5 == 0:
        #         result.append('Buzz')
        #     else: 
        #         result.append(str(i))
        # return result
        return ['Fizz' * (not i%3) + 'Buzz' * (not i%5) or str(i) for i in range(1, n+1) ]

obj = Solution();
print obj.fizzBuzz(15)

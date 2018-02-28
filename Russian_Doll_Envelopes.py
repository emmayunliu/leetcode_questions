# https://leetcode.com/problems/russian-doll-envelopes/description/
# import bisect
# class Solution(object):
#     def maxEnvelopes(self, envelopes):
#         """
#         :type envelopes: List[List[int]]
#         :rtype: int
#         """
#         if len(envelopes) < 2:
#             return len(envelopes)

#         sort = sorted(envelopes)
#         result = []
#         for index, item in sort:
#             item
#         return len(result)
            

# envelopes = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
# obj = Solution()
# print obj.maxEnvelopes(envelopes)


import bisect

# class Solution(object):
#     def maxEnvelopes(self, envelopes):
#         # Get value of height sorted by width
#         sortedSingles = [a[1] for a in sorted(envelopes, key = lambda x: (x[0], -x[1]))]
#         print sortedSingles
#         # Results array to store sorted, length to return 
#         results, length = [0] * len(sortedSingles), 0
#         # Loop through sorted widths
#         for x in sortedSingles:
#             # Get proper index for single and insert
#             i = bisect.bisect_left(results, x, 0, length)
#             results[i] = x
#             print i, x, results
#             # Length = i + 1
#             if i == length:
#                 length += 1
#         return length
# envelopes = [[1,100],[5,200],[5,300],[5,500],[5,400],[5,250],[5,370],[5,360],[5,380]]
# result = Solution() 
# print result.maxEnvelopes(envelopes)

test = [1,2,5,5,8]
index = bisect.bisect(test, 5, 0, 3)
test[index] = 5
print index, test
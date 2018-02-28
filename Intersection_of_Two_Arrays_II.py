# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # shortNums = sorted(nums2) if len(nums1) >= len(nums2) else sorted(nums1)
        # longNums = sorted(nums2) if len(nums1) < len(nums2) else sorted(nums1)
        # result = []
        # for i in shortNums:
        #     if i in longNums:
        #         result.append(i)
        #         longNums.remove(i)
        # return result
        counts = collections.Counter(nums1)
        result = []
        for i in nums2:
            if counts[i] > 0:
                result.append(i)
                counts[i] -= 1
        return result

obj = Solution()
print obj.intersect([1,2], [1,1])
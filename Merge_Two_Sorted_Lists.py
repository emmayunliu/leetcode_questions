# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = newList = ListNode(0)
        while l1 and l2: 
            if l1.val < l2.val:
                newList.next = l1
                l1 = l1.next
            else:
                newList.next = l2
                l2 = l2.next
            newList = newList.next
        newList.next = l1 or l2
        return result.next
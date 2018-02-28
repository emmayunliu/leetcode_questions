# https: // leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # find mid point
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            next = slow.next
            slow.next = node
            node = slow
            slow = next
        # compare the first and second half
        while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True

            
        
        
            
                


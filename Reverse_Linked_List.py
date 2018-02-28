# https://leetcode.com/problems/reverse-linked-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head is None or head.next is None:
        #     return head
        # node = ListNode(head.val)
        # while head.next:
        #     nextNode = ListNode(head.next.val)
        #     nextNode.next = node
        #     node = nextNode
        #     head = head.next
        # return nextNode
        prev = None
        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current
        print prev.val, prev.next.val
        return prev

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
test = Solution()
print test.reverseList(list)

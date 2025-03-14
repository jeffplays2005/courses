# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head.next == None:
            return None
        # Faster is n ahead of slow
        faster = head
        slow = head
        counter = 0
        # Progress fast
        while counter < n:
            faster = faster.next
            counter += 1
        if faster == None:
            return head.next
        while faster.next != None:
            faster = faster.next
            slow = slow.next
        slow.next = slow.next.next
        return head

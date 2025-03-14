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
        if not head.next and n == 1:
            return None
        p1 = 0
        p2 = 0
        secondary = head
        while secondary != None:
            secondary = secondary.next
            p2 += 1
        diff = p2 - n
        if p2 == n:
            return head.next
        head1 = head
        head2 = head
        while p1 < diff:
            p1 += 1
            head1 = head2
            head2 = head2.next
        head1.next = head2.next
        return head

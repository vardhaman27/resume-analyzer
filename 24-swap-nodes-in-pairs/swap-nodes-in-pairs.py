# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        prev = None
        first = head
        second = head.next
        while first is not None and second is not None:
            third = second.next
            second.next = first
            first.next = third

            if prev is None:
                head = second 
            else:
                prev.next = second
            prev = first
            first = third
            if third:
                second = third.next 
            else: 
                second = None
        return head

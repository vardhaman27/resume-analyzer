# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp = head
        lenn = 0
        while temp:
            lenn += 1
            temp = temp.next
        a = lenn - n
        if a == 0:
            new_head = head.next
            return new_head
        temp = head
        c =  1
        while c < a:
            temp = temp.next
            c += 1
        temp.next = temp.next.next
        return head
        



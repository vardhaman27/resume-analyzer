# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        curr = head
        s = ""
        while curr:
            s += str(curr.val)
            curr = curr.next
        return int(s, 2)
            
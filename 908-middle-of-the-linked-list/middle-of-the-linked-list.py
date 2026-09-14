# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        n = 0
        temp = head
        while temp is not None:
            n += 1
            temp = temp.next
        temp = head
        for i in range(0, n//2):
            temp = temp.next
        return temp
    
        
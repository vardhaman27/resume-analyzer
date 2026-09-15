# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        temp = head.next
        dummy = ListNode(0)
        curr = dummy

        while temp is not None:
            summ = 0

            while temp.val != 0:
                summ += temp.val
                temp = temp.next

            curr.next = ListNode(summ)
            curr = curr.next
            temp = temp.next
        return dummy.next



        
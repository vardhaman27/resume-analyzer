# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
        head2 = prev
        max_sum = 0
        while head2:
            max_sum = max(max_sum, head.val + head2.val)
            head = head.next
            head2 = head2.next
        return max_sum
        
        


        
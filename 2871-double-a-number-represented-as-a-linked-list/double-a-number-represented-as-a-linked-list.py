# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        curr =  head
        ans = head
        s = ""
        while head:
            s += str(head.val)
            head = head.next
        
        m = str(int(s)*2)
        if len(m) > len(s):
            ans = ListNode(0)
            ans.next = curr
            curr = ans

        for i in m:
            curr.val = int(i)
            if curr.next:
                curr = curr.next

        return ans
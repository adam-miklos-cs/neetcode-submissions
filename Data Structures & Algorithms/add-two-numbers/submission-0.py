# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        p = ans
        p1 = l1
        p2 = l2
        overflow = 0
        while p1 and p2:
            p.next = ListNode()
            p = p.next

            c = p1.val + p2.val + overflow
            p.val = c % 10
            overflow = c // 10

            p1 = p1.next
            p2 = p2.next
            
        
        while p1:
            p.next = ListNode()
            p = p.next
            c = p1.val + overflow
            p.val = c % 10
            overflow = c // 10
            p1 = p1.next

        while p2:
            p.next = ListNode()
            p = p.next
            c = p2.val + overflow
            p.val = c % 10
            overflow = c // 10
            p2 = p2.next

        if overflow:
            p.next = ListNode()
            p.next.val = 1

        return ans.next



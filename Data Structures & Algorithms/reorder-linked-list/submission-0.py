# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        c = head
        while c is not None:
            n = c.next
            c.next = p
            p = c
            c = n
        return p
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        p1 = head
        s = head
        f = head
        while f and f.next and f.next.next:
            f = f.next.next
            s = s.next
        
        p2 = s.next
        s.next = None

        p2 = self.reverseList(p2)

        while p1 and p2:
            temp = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p1.next.next
            p2 = temp

        
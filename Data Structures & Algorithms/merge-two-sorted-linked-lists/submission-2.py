# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        if l2.val < l1.val:
            l1, l2 = l2, l1
        
        p1 = l1
        p2 = l2

        while p1.next and p2:
            if p1.next.val > p2.val:
                to_insert = p2
                p2 = p2.next
                to_insert.next = p1.next
                p1.next = to_insert
            p1 = p1.next

        if p2:
            p1.next = p2
        
        return l1
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        p1 = l1
        p2 = l2

        ans = ListNode()
        current = ans
        
        while p1 and p2:
            if p1.val <= p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            
            current = current.next
        
        current.next = p1 if p1 else p2
        
        return ans.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if not n:
            return None
        l = lists[0]
        for i in range(1, n):
            l = self.mergeTwoLists(l, lists[i])
        return l
        
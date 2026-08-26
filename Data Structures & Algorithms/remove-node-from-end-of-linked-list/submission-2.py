# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans = ListNode()
        ans.next = head

        l = ans
        r = ans
        for i in range(n + 1):
            r = r.next
        
        while r:
            l = l.next
            r = r.next

        temp = l.next
        l.next = l.next.next
        temp.next = None
        
        return ans.next
        


        
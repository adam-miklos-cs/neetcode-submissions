# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            groupEnd = groupPrev
            for _ in range(k):
                groupEnd = groupEnd.next
                if groupEnd is None:
                    break
            
            if groupEnd is None:
                break
                
            groupStart = groupPrev.next
            nextGroup = groupEnd.next
            
            groupEnd.next = None
            
            self.reverseList(groupStart)
            
            groupPrev.next = groupEnd       
            groupStart.next = nextGroup     
            
            groupPrev = groupStart
            
        return dummy.next
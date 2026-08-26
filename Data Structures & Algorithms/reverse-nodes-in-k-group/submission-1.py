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
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Find the first window
        l1 = r1 = head
        c = 1
        while (r1 is not None) and (c < k):
            r1 = r1.next
            c += 1
        if r1 is None:
            return None
        
        # Save the next window
        l2 = r2 = r1.next

        r1.next = None
        self.reverseList(l1)
        l1, r1 = r1, l1
        head = l1 # ?

        while l2 is not None:
            c = 1
            while (r2 is not None) and (c < k):
                r2 = r2.next
                c += 1
            if r2 is None:
                r1.next = l2
                return head
        
            
            r1.next = r2
            temp = r2.next
            r2.next = None
            self.reverseList(l2)

            l1, r1 = r2, l2
            l2 = r2 = temp

            #print(l1.val)
            #print(r1.val)
            #print(l2.val)
            #print(r2.val)

        return head



            
        
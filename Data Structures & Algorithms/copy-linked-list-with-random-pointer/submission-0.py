"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Initializing deep copy nodes
        p = head
        while p:
            n = p.next
            p.next = Node(p.val)
            p.next.next = n
            p = n
        
        # Setting deep copy values
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            else:
                p.next.random = None
            p = p.next.next


        # Extracting deep copy
        p1 = head
        p2 = head.next

        ans = p2

        while p2.next:
            p1.next = p1.next.next
            p2.next = p2.next.next
            p1 = p1.next
            p2 = p2.next
        
        p1.next = None

        return ans
            
        
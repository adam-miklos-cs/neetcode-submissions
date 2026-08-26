"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, start_node: Optional['Node']) -> Optional['Node']:
        # BFS + Creating the nodes for the deep copy if they don't exist
        if not start_node:
            return None
        
        start_node_copy = Node(start_node.val, [])

        d = deque()
        d.append(start_node)

        copies = {}
        copies[start_node] = start_node_copy

        while d:
            node = d.popleft()
            for neighbor in node.neighbors:
                neighbor_copy = copies.get(neighbor, None)
                if not neighbor_copy:
                    d.append(neighbor)
                    neighbor_copy = Node(neighbor.val, [])
                    copies[neighbor] = neighbor_copy
                copies[node].neighbors.append(neighbor_copy)
        
        return start_node_copy

        

        
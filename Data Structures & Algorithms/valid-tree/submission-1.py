class DSU:
    def __init__(self, n: int):
        # Initially, each node is its own parent (n disjoint sets)
        self.parent = list(range(n))
        # Rank tracks the upper bound of the tree height for each root
        self.rank = [0] * n
        # Tracks the current number of connected components
        self.components = n

    def find(self, x: int) -> int:
        # Path Compression: make every visited node point directly to the root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        # If they already share the same root, an edge between them forms a cycle!
        if root_x == root_y:
            return False

        # Union by Rank: attach the shorter tree under the taller tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.components -= 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        dsu = DSU(n)

        for [u, v] in edges:
            if not dsu.union(u, v):
                return False
        
        return True


        
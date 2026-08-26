import heapq as hq
class Solution:
    def networkDelayTime(self, connections: List[List[int]], n: int, k: int) -> int:
        # Shortest path from one node to all the other
        # Directed edges
        # Positive weights

        MAX_D = 1e6

        al = [[] for _ in range(n + 1)]
        for connection in connections:
            al[connection[0]].append([connection[2], connection[1]])

        d = [MAX_D] * (n + 1)
        d[k] = 0

        q = []
        hq.heapify(q)
        hq.heappush(q, (d[k], k))

        while q:
            node = q[0]
            hq.heappop(q)
            if node[0] > d[node[1]]:
                continue
            for edge in al[node[1]]:
                if node[0] + edge[0] < d[edge[1]]:
                    d[edge[1]] = node[0] + edge[0] 
                    hq.heappush(q, (d[edge[1]], edge[1]))
        
        res = 0
        for i in range(1, n + 1):
            if d[i] == MAX_D:
                return -1
            res = max(res, d[i])

        return res
            


        
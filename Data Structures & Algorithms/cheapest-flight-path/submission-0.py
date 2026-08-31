class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
    
        p = [[INF] * n for _ in range(k + 2)]
        p[0][src] = 0
    
        for i in range(1, k + 2):
            p[i] = p[i - 1][:]
            
            for u, v, w in flights:
                if p[i - 1][u] != INF:
                    p[i][v] = min(p[i][v], p[i - 1][u] + w)
    
        return -1 if p[k + 1][dst] == INF else int(p[k + 1][dst])
        
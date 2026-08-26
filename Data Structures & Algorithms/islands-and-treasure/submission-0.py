class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m = len(grid)
        n = len(grid[0])
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        dq = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dq.append((i, j))

        while dq:
            (i, j) = dq.popleft()

            for d in dirs:
                n_i, n_j = i + d[0], j + d[1]
                if 0 <= n_i < m and 0 <= n_j < n and grid[n_i][n_j] == INF:
                    grid[n_i][n_j] = grid[i][j] + 1
                    dq.append((n_i, n_j))
        
        
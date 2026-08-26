class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        dq = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    grid[i][j] = 0
                    dq.append((i, j))
                elif grid[i][j] == 1:
                    grid[i][j] = -1
                else:
                    grid[i][j] = -2
        

        while dq:
            (i, j) = dq.popleft()

            for d in dirs:
                n_i, n_j = i + d[0], j + d[1]
                if 0 <= n_i < m and 0 <= n_j < n and grid[n_i][n_j] == -1:
                    grid[n_i][n_j] = grid[i][j] + 1
                    dq.append((n_i, n_j))

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    return -1
                ans = max(ans, grid[i][j])

        return ans
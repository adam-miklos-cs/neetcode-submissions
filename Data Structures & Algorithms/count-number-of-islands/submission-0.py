class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        island_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island_count += 1
                    # dfs 
                    s = deque()
                    s.append((i, j))
                    while s:
                        (y, x) = s.pop()
                        if grid[y][x] == "0":
                            continue
                        
                        grid[y][x] = 0
                        
                        for d in dirs:
                            next_y, next_x = y + d[0], x + d[1]
                            if (0 <= next_y < m and 
                                0 <= next_x < n and 
                                grid[next_y][next_x] == "1"):
                                s.append((next_y, next_x))

        return island_count
        
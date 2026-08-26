class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    area = 0
                    # dfs 
                    s = deque()
                    s.append((i, j))
                    while s:
                        (y, x) = s.pop()
                        if not grid[y][x]:
                            continue
                        
                        grid[y][x] = 0
                        area += 1
                        
                        for d in dirs:
                            next_y, next_x = y + d[0], x + d[1]
                            if (0 <= next_y < m and 
                                0 <= next_x < n and 
                                grid[next_y][next_x]):
                                s.append((next_y, next_x))
                    max_area = max(max_area, area)

        return max_area
        
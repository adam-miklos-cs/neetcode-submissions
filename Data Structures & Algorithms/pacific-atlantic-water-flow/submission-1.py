class Solution:
    def pacificAtlantic(self, hs: List[List[int]]) -> List[List[int]]:
        m = len(hs)
        n = len(hs[0])

        s = deque()
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        pacific = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            pacific[i][0] = True
            s.append((i, 0))
        for j in range(n):
            pacific[0][j] = True
            s.append((0, j))

        while s:
            i, j = s.pop()
            for d in dirs:
                ii = i + d[0]
                jj = j + d[1]

                if 0 <= ii < m and 0 <= jj < n and not pacific[ii][jj] and hs[ii][jj] >= hs[i][j]:
                    pacific[ii][jj] = True
                    s.append((ii, jj))



        atlantic = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            atlantic[i][n - 1] = True
            s.append((i, n-1))
        for j in range(n):
            atlantic[m - 1][j] = True
            s.append((m-1, j))
        
        while s:
            i, j = s.pop()
            for d in dirs:
                ii = i + d[0]
                jj = j + d[1]

                if 0 <= ii < m and 0 <= jj < n and not atlantic[ii][jj] and hs[ii][jj] >= hs[i][j]:
                    atlantic[ii][jj] = True
                    s.append((ii, jj))

        ans = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])
        
        return ans
            
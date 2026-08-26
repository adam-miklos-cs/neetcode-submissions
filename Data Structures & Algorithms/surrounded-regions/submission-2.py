class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        s = deque()

        for i in range(m):
            if board[i][0] == "O":
                s.append((i, 0))
                board[i][0] = "E"
            if board[i][n - 1] == "O":
                s.append((i, n - 1))
                board[i][n - 1] = "E"

        for j in range(n):
            if board[0][j] == "O":
                s.append((0, j))
                board[0][j] = "E"
            if board[m - 1][j] == "O":
                s.append((m - 1, j))
                board[m - 1][j] = "E"

        while s:
            i, j = s.pop()

            for d in dirs:
                ii, jj = i + d[0], j + d[1]
                if 0 <= ii < m and 0 <= jj < n and board[ii][jj] == "O":
                    s.append((ii, jj))
                    board[ii][jj] = "E"
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "E":
                    board[i][j] = "O"

        
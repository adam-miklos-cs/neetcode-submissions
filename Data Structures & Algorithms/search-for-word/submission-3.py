class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(i: int, j: int, index: int) -> bool:
            nonlocal board
            nonlocal m
            nonlocal n
            nonlocal word

            ans = False

            if index == len(word):
                return True
            
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            
            if board[i][j] == '#':
                return False
            
            if word[index] != board[i][j]:
                return False

            c = board[i][j]

            board[i][j] = '#'
            
            for d in dirs:
                ans = ans | search(i + d[0], j + d[1], index + 1)
            
            board[i][j] = c

            return ans

        m = len(board)
        n = len(board[0])

        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        ans = False
        for i in range(0, m):
            for j in range(0, n):
                ans = ans | search(i, j, 0)

        return ans
        
        
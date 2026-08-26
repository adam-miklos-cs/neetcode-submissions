class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(i: int, j: int, index: int) -> bool:
            nonlocal board
            nonlocal m
            nonlocal n
            nonlocal word
            nonlocal seen

            ans = False

            if index == len(word):
                return True
            
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            
            if seen[i][j]:
                return False
            
            if word[index] != board[i][j]:
                return False

            seen[i][j] = True
            
            for d in dirs:
                ans = ans | search(i + d[0], j + d[1], index + 1)
            
            seen[i][j] = False

            return ans

        m = len(board)
        n = len(board[0])

        seen = [[0] * n for _ in range(m)]
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        ans = False
        for i in range(0, m):
            for j in range(0, n):
                ans = ans | search(i, j, 0)

        return ans
        
        
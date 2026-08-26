class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        occupied_row = [False] * n
        occupied_col = [False] * n
        occupied_main_diag = [False] * (2 * n - 1)
        occupied_second_diag = [False] * (2 * n - 1)
        def generator(i: int, build: List[List[str]]):
            if i == n:
                ans.append(["".join(row) for row in build])
                return
            
            for j in range(0, n):
                if (not occupied_row[i] and 
                    not occupied_col[j] and 
                    not occupied_main_diag[i - j + (n - 1)] and
                    not occupied_second_diag[i + j]):

                    build[i][j] = 'Q'
                    occupied_row[i] = True
                    occupied_col[j] = True
                    occupied_main_diag[i - j + (n - 1)] = True
                    occupied_second_diag[i + j] = True

                    generator(i + 1, build)

                    build[i][j] = '.'
                    occupied_row[i] = False
                    occupied_col[j] = False
                    occupied_main_diag[i - j + (n - 1)] = False
                    occupied_second_diag[i + j] = False
                    
        build = [['.' for _ in range(n)] for _ in range(n)]
        generator(0, build)

        return ans





        
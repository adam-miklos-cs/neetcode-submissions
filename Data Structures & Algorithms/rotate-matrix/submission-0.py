class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 90 degree clockwise means: transpose + swap row elements
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for i in range(n):
            matrix[i].reverse()

    
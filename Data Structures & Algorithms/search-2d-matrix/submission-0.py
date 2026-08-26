class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, m * n
        while l + 1 < r:
            mid = l + (r - l) // 2
            i = mid // n
            j = mid % n
            if matrix[i][j] <= target:
                l = mid
            else:
                r = mid

        i = l // n
        j = l % n
        if matrix[i][j] == target:
            return True
        return False

        
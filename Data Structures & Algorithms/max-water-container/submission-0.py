class Solution:
    def maxArea(self, h: List[int]) -> int:
        l = 0
        r = len(h) - 1
        ans = 0
        while l < r:
            if h[l] <= h[r]:
                ans = max(ans, (r - l) * h[l])
                l += 1
            else:
                ans = max(ans, (r - l) * h[r])
                r -= 1
        return ans


        
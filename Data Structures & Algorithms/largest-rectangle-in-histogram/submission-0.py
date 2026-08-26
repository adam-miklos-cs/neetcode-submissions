class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        h.append(0)
        n = len(h)
        s = deque()
        ans = 0
        for i in range(n):
            j = i
            while s and h[i] <= s[-1][0]:
                j = s[-1][1]
                ans = max(ans, s[-1][0] * (i - j))
                s.pop()
            s.append((h[i], j))
        return ans
         
         
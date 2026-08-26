class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        ans = 0
        d = {}
        for r in range(n):
            if s[r] in d:
                l = max(d[s[r]] + 1, l)
            d[s[r]] = r
            ans = max(ans, r - l + 1)
        return ans
            
        
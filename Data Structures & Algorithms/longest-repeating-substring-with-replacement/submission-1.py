class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        
        count = {}
        ans = 0

        l = 0
        maxf = 0

        for r in range(n):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])

            while k + maxf < r - l + 1:
                count[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1) 
        return ans

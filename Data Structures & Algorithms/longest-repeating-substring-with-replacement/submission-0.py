class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        d = {}
        distinct_count = 0
        ans = 0
        max_key = s[0]
        d[max_key] = 1
        for r in range(1, n):
            d[s[r]] = d.setdefault(s[r], 0) + 1
            if d[s[r]] > d[max_key]:
                max_key = s[r]
        
            while k < r-l+1 - d[max_key]:
                d[s[l]] -= 1
                if max_key == s[l]:
                    max_key = max(d, key=d.get)
                        
                l += 1
            ans = max(ans, r - l + 1) 
        return ans

       # k >= (r-l+1) - max #SameChar 
       # max #Same Char-t hogyan kapom meg? 
       # Minden pillanatban hosszan megyek a dict-en es megnezem?
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        for c in s1:
            s1_count[c] = 1 + s1_count.get(c, 0)
        
        n = len(s2)
        s2_count = {}
        l = 0
        
        for r in range(n):
            s2_count[s2[r]] = 1 + s2_count.get(s2[r], 0)
            
            while s2_count[s2[r]] > s1_count.get(s2[r], 0):
                s2_count[s2[l]] -= 1
                l += 1
            
            if (r - l + 1) == len(s1):
                return True
                
        return False
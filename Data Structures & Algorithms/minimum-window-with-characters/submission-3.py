class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Process t
        m = len(t)

        count_t = {} 
        distinct_goals = 0

        for i in range(m):
            last_val = count_t.get(t[i], 0)
            if last_val == 0:
                distinct_goals += 1
            count_t[t[i]] = 1 + last_val

        # Process s
        n = len(s)

        l = 0 
        count_s = {}
        reached = 0
        ans_start = -1
        ans_end = n

        for r in range(n):
            count_s[s[r]] = 1 + count_s.get(s[r], 0)

            if count_s[s[r]] == count_t.get(s[r], 0):
                reached += 1

            if reached == distinct_goals:
                while l <= r and count_s[s[l]] > count_t.get(s[l], 0):
                        count_s[s[l]] -= 1
                        l += 1
                
                if r - l < ans_end - ans_start:
                    ans_start = l
                    ans_end = r


        
        if ans_start == -1:
            return ""
        else:
            return s[ans_start : ans_end + 1]

             

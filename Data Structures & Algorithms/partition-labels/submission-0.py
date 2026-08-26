class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s) 
        last_pos = {}
        for i in range(n - 1, -1, -1):
            if s[i] in last_pos:
                continue
            last_pos[s[i]] = i
        
        current_start = 0
        current_end = last_pos[s[0]]
        ans = []
        for i in range(0, n):
            if i == current_end:
                ans.append(current_end - current_start + 1)
                if i < n - 1:
                    current_start = i + 1
                    current_end = last_pos[s[current_start]]
            current_end = max(current_end, last_pos[s[i]])
        return ans


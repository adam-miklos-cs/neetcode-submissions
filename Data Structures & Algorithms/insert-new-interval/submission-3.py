class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]
        i = 0
        ans = []
        while i < n and intervals[i][0] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        # Handle left
        if i > 0 and newInterval[0] <= ans[i - 1][1]:
            ans[i - 1][1] = max(ans[i - 1][1], newInterval[1])
        else:
            ans.append(newInterval)
        
        print(ans)
        print(i)
        # Handle right
        while i < n:
            if intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])
            i += 1

        return ans
            
        
        
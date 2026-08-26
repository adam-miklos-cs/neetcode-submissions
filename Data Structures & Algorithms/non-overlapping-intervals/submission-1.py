class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: (x[1], x[0]))
        print(intervals)
        stk = deque()
        stk.append(intervals[0]) 
        for i in range(1, n):
            if intervals[i][0] >= stk[-1][1]:
                stk.append(intervals[i])

        return n - len(stk)

            
        
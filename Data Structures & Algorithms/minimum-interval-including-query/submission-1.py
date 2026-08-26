import heapq as hq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])    
        i = 0
        q = []
        ans = [-1] * len(queries)
        for (time, index) in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= time:
                hq.heappush(q, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            while len(q) and time > q[0][1]:
                hq.heappop(q)
            if len(q):
                ans[index] = q[0][0]
            
        return ans
            

            

        
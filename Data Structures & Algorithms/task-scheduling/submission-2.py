import heapq as hq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        h = []
        for i in range(0, 26):
            if count[i]:
                hq.heappush(h, -count[i])
        
        t = 0
        dq = deque()

        while len(h) or len(dq):
            while len(dq) and t - dq[0][1] - 1 >= n:
                hq.heappush(h, dq[0][0])
                dq.popleft()

            if len(h):
                top = hq.heappop(h)
                if top < -1:
                    dq.append((top + 1, t))
            t += 1

        return t


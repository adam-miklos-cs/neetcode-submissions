class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        s = deque()
        result = [0] * n
        for i in range(n - 1, -1, -1):
            while s and t[i] >= t[s[-1]]:
                s.pop()
            if s:
                result[i] = s[-1] - i
            s.append(i)
        return result

        
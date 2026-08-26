import bisect
class TimeMap:

    def __init__(self):
       self.d = defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect_right(self.d[key], timestamp, key=lambda x: x[0])
        if i == 0:
            return ""
        else:
            return self.d[key][i - 1][1]
        

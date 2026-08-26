class Solution:
    def isValid(self, s: str) -> bool:
        dq = deque()
        for c in s:
            if c in {'(', '[', '{'}:
                dq.append(c)
            elif c == ')' and dq and dq[-1] == '(':
                dq.pop()
            elif c == ']' and dq and dq[-1] == '[':
                dq.pop()
            elif c == '}' and dq and dq[-1] == '{':
                dq.pop()
            else:
                return False
        return len(dq) == 0
            

        
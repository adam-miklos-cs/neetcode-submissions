class Solution:
    EMPTY = 201
    def evalRPN(self, tokens: List[str]) -> int:
        s = deque()
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                s.append(int(token))
            else:
                if len(s) < 2:
                    print("ERROR")
                else:
                    o2 = s.pop()
                    o1 = s.pop()
                    if token == '+':
                        s.append(o1 + o2)
                    elif token == '-':
                        s.append(o1 - o2)
                    elif token == '*':
                        s.append(o1 * o2)
                    elif token == '/':
                        s.append(int(o1 / o2))
                    else:
                        print("ERROR")
        return s[-1]
            
        
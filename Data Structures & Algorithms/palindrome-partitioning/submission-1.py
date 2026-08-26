class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        is_palindrome = []
        for i in range(0, n):
            l = [False] * n
            for j in range(0, i + 1):
                l[j] = True
            is_palindrome.append(l)
        
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                is_palindrome[i][j] = ((s[i] == s[j]) and is_palindrome[i + 1][j - 1])

        ans = []
        
        def split(start: int, build: List[str]):
            if start == n:
                ans.append(build.copy())
                return
            
            for end in range(start, n):
                if is_palindrome[start][end]:
                    build.append(s[start:end + 1])
                    split(end + 1, build)
                    build.pop()
        
        split(0, [])
        return ans
                    
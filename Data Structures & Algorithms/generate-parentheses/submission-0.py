class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(open_count: int, close_count: int, build: str):
            nonlocal ans

            print(build)

            if open_count == 0 and close_count == 0:
                ans.append(build)
                return
            
            if open_count:
                helper(open_count - 1, close_count, build + '(')
            
            if open_count < close_count:
                helper(open_count, close_count - 1, build + ')')
        
        helper(n, n, "")
        return ans

        
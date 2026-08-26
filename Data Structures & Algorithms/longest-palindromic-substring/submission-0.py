class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans_len = 1
        ans_i = n - 1
        dp = [True] * (n + 1)
        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                dp[j] = (s[i] == s[j]) and dp[j - 1]
                if dp[j] and (j - i + 1 > ans_len):
                    ans_len = j - i + 1
                    ans_i = i

        return s[ans_i : ans_i + ans_len]
            

        
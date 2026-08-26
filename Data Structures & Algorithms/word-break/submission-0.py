class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
       
class Solution:
    def insert(self, word: str, root: TrieNode) -> None:
        cur = root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for word in wordDict:
            self.insert(word, root)
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        for i in range(n - 1, -1, -1):
            cur = root
            for j in range(i, n):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.end_of_word and dp[j + 1]:
                    dp[i] = True
                    break
        return dp[0]


        
        
class TrieNode:
    def __init__(self, word: Optional[str] = None):
        self.children = {}
        self.word = word

class Solution:
    def __init__(self):
        self.start_node = TrieNode()

    def addWord(self, word: str) -> None:
        current_node = self.start_node
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.word = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])

        for word in words:
            self.addWord(word)

        ans = []
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def search(current_node: TrieNode, i: int, j: int):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            
            if board[i][j] == '.':
                return

            if board[i][j] not in current_node.children:
                return

            current_node = current_node.children[board[i][j]]
            if current_node.word:
                ans.append(current_node.word)
                current_node.word = None

            val = board[i][j]
            board[i][j] = '.'
            
            for d in dirs:
                search(current_node, i + d[0], j + d[1])

            board[i][j] = val

        for i in range(m):
            for j in range(n):
                search(self.start_node, i, j)
        
        return ans



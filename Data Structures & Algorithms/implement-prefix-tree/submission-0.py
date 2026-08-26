class PrefixTree:

    def __init__(self):
        self.empty_node = {}

    def insert(self, word: str) -> None:
        current_node = self.empty_node
        for char in word:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
        current_node['\n'] = True


    def search(self, word: str) -> bool:
        current_node = self.empty_node
        for char in word:
            if char not in current_node:
                return False
            current_node = current_node[char]
        
        return current_node.get('\n', False)
        

    def startsWith(self, prefix: str) -> bool:
        current_node = self.empty_node
        for char in prefix:
            if char not in current_node:
                return False
            current_node = current_node[char]
        return True
        
        
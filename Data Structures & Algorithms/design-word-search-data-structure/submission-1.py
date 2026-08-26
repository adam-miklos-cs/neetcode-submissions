class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:
    def __init__(self):
        self.start_node = TrieNode()

    def addWord(self, word: str) -> None:
        current_node = self.start_node
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.end_of_word = True
        

    def search(self, word: str) -> bool:
        n = len(word)
        def rec_search(current_node: TrieNode, i: int) -> bool:
            while i < n:
                if word[i] == '.':
                    accum = False
                    for node in current_node.children.values():
                        accum = accum | rec_search(node, i + 1)
                    return accum
                else:
                    if word[i] not in current_node.children:
                        return False
                    current_node = current_node.children[word[i]]
                    i += 1
            
            return current_node.end_of_word
        return rec_search(self.start_node, 0)
        

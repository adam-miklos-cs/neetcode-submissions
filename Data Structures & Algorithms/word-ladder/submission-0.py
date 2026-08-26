class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(list)
        m = len(beginWord) 

        # Wildcard logic
        for word in wordList:
            for i in range(m):
                changed = word[0 : i] + "*" + word[(i + 1) : m]
                d[changed].append(word)

        # BFS
        q = deque()
        q.append((beginWord, 1))
        seen = {}
        while q:
            word, dist = q.popleft()
            for i in range(m):
                changed = word[0 : i] + "*" + word[(i + 1) : m]
                for match in d[changed]:
                    if match == endWord:
                        return dist + 1

                    if not seen.get(match, False):
                        seen[match] = True
                        q.append((match, dist + 1))

                d[changed].clear()

        return 0
                
                


        

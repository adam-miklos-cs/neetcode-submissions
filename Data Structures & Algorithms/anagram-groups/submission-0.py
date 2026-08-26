from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for str in strs:
            count = [0] * 26 
            for c in str:
                ind = ord(c) - ord('a')
                count[ind] += 1
            signature = tuple(count)
            groups[signature].append(str)

        return list(groups.values())
         
                
        
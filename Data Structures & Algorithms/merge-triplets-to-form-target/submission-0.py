class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        LEN = 3
        res = [-1] * LEN
        for triplet in triplets:
            is_bad_triple = False
            for i in range(0, LEN):
                if triplet[i] > target[i]:
                    is_bad_triple = True
                    break
            if is_bad_triple:
                continue
            for i in range(0, LEN):
                res[i] = max(res[i], triplet[i])
        return res == target 

        
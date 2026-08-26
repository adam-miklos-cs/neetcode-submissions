class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        permutations = []
        def generatePermutations(i: int, included: int, permutation: List[int]):
            nonlocal nums
            nonlocal n
            nonlocal permutations

            if i == n:
                permutations.append(permutation.copy())
            
            for j in range(0, n):
                if included & (1 << j):
                    continue
                permutation.append(nums[j])
                generatePermutations(i + 1, included | (1 << j), permutation)
                permutation.pop()


        generatePermutations(0, 0, [])
        return permutations
        
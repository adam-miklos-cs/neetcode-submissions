class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Straightforward way:
        # Count frequencies associated with elements
        # Sort by frequency
        # Return the k most frequent
        # ~ O(n logn)

        # Another approach could be using a data structure
        # In C++ a multiset might help but it seems kinda complicated
        # not sure if it would work.
        # The problem is that you have to be able to make the
        # frequency of an element bigger easily.
        # But it also have to be ordered by the frequencies.
        # I don't what DS can do this.
        # I mean dictionaries are not ordered in any means.
        # Self-balanced BT can be but with the key not the value, right?
        # You can do two sided stuff  but at a given moment it is not guaranteed
        # that you won't have different elements with the same frequency. So idk.

        frequencies = dict()
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        
        n = len(nums)
        bucket = [[] for _ in range(1, n + 2)]

        for num, frequency in frequencies.items():
            bucket[frequency].append(num)
        
        top_k = []
        for frequency in range(n, 0, -1):
            for num in bucket[frequency]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k


         
        

            

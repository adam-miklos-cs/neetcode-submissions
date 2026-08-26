from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Inputs:
            nums: An array of integers.
            
        Outputs:
            bool: True if any value appears at least twice in the array, False otherwise.

        Intuition & Data Structure Selection:
            Goal: Traverse the array while maintaining a history of seen elements, 
                  requiring the fastest possible membership check.

            1. Tree-based approach (e.g., C++ `std::set`): 
               Implemented as a self-balancing binary search tree (Red-Black Tree). 
               Insertions and lookups are O(log n). 
               Total Time: O(n log n).
               
            2. Hash-based approach (e.g., C++ `std::unordered_set` or Python `set`): 
               Implemented as a Hash Table. The memory index is calculated deterministically 
               from the value's hash. Insertions and lookups are O(1) on average.
               Total Time: O(n).

        Complexity Analysis:
            Time Complexity: O(n) average. We iterate through the array of size `n` at most once. 
                             The `in` check and `.add()` operation in a Python set take O(1) average time.
            Space Complexity: O(n) worst-case. The hash table must allocate continuous memory 
                              to store up to `n` unique elements if no duplicates exist.
        """
        seen_numbers = set()
        
        for num in nums:
            if num in seen_numbers:
                return True
            seen_numbers.add(num)
            
        return False
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Method: Hash Map (Complement Search)
        
        Inputs: 
            nums: List[int] - Unordered sequence of integers.
            target: int - The required sum constraint.
            
        Outputs: 
            List[int] - A 2-element list containing the original indices.
            
        Intuition: 
            Iterates through `nums`, computing the required `complement` for each element. 
            Uses a hash map to achieve O(1) lookups for previously seen elements, bypassing 
            the need to sort or use nested loops.
            
        Time Complexity: O(n) - We traverse the list containing n elements exactly once.
        Space Complexity: O(n) - The hash map stores at most n elements.
        """
        seen = {}  
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
                
            seen[num] = i
            
        return []
    
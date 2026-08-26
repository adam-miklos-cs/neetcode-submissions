class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        
    
        l, r = -1, m + 1
        k = (m + n + 1) // 2

        while l + 1 < r:
            i = l + (r - l) // 2
            j = k - i

            A_left = nums1[i - 1] if i > 0 else float('-inf')
            B_right = nums2[j] if j < n else float('inf')

            if A_left <= B_right:
                l = i  
            else:
                r = i  

        
        i = l
        j = k - i

        A_left = nums1[i - 1] if i > 0 else float('-inf')
        A_right = nums1[i] if i < m else float('inf')
        B_left = nums2[j - 1] if j > 0 else float('-inf')
        B_right = nums2[j] if j < n else float('inf')

        if (m + n) % 2 == 1:
            return float(max(A_left, B_left))
        
        return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
        
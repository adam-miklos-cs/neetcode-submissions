class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1) Filter non-alphanumerical characters and transform uppercase 
        # characters to lowercase.
        # 2) Two pointers

        transformed = re.sub(r'[^a-zA-Z0-9]', '', s).lower() 

        s = 0
        e = len(transformed) - 1

        while s < e:
            if transformed[s] != transformed[e]:
                return False
            s += 1
            e -= 1
        
        return True
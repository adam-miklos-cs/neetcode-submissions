class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        parenthes_count = 0
        star_count = 0
        for i in range(0, n):
            if s[i] == '(':
                parenthes_count += 1
            elif s[i] == '*':
                star_count += 1
            else:
                if parenthes_count:
                    parenthes_count -= 1
                elif star_count:
                    star_count -= 1
                else:
                    return False
        
        parenthes_count = 0
        star_count = 0

        for i in range(n - 1, -1, -1):
            if s[i] == ')':
                parenthes_count += 1
            elif s[i] == '*':
                star_count += 1
            else:
                if parenthes_count:
                    parenthes_count -= 1
                elif star_count:
                    star_count -= 1
                else:
                    return False
        
        return True


        
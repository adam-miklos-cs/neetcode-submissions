class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        digit_to_letters = defaultdict(list)
        current_letter = 'a'
        for digit in range(2, 10):
            if digit == 7 or digit == 9:
                letters_mapped = 4
            else:
                letters_mapped = 3
            
            while letters_mapped:
                digit_to_letters[digit].append(current_letter)
                current_letter = chr(ord(current_letter) + 1)
                letters_mapped -= 1
        
        ans = []
        n = len(digits)

        def generateCombinations(i: int, combination: str):
            if i == n:
                ans.append(combination)
                return
            
            for letter in digit_to_letters[int(digits[i])]:
                generateCombinations(i + 1, (combination + letter))
        
        generateCombinations(0, "")

        return ans

            


        
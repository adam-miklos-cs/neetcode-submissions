class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        IN: String s, String t (Length N)
        OUT: Boolean (True if character frequency maps are isomorphic, False otherwise)
        
        KEY CONCEPTS: 
        1. Frequency Counting: Building a hash map of character occurrences.
        2. Interpreter Overhead: Manual `for` loops in pure Python are slow due to 
           bytecode evaluation and integer object creation per iteration.
        3. Memory Layout: Python `dict` is a highly optimized C-level hash table, 
           making it strictly superior to a manual 26-length array which requires 
           expensive `ord()` math in Python.
        """ 

        if len(s) != len(t):
            return False

        count_s = dict()
        count_t = dict()

        # Manual iteration: Carries Python interpreter overhead
        for c in s:
            count_s[c] = count_s.get(c, 0) + 1

        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        # C-Delegation: The `==` operator maps to Python's internal `dict_richcompare`
        # in C, bypassing manual key iteration overhead.
        return count_s == count_t
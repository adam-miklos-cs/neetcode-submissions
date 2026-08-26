from collections import defaultdict
from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Method: Frequency Signature Hashing

        Inputs:
            strs: List[str] - An array of strings composed of lowercase English letters.

        Outputs:
            List[List[str]] - A list of sublists, where each sublist contains grouped anagrams.

        Main Idea:
            Two strings are anagrams if and only if their character frequencies are identical.
            Instead of sorting each string (which costs O(m log m)), we compute a fixed-size
            frequency array of length 26 for each string. Converting this array into an
            immutable tuple creates a deterministic, order-independent signature. We use this
            signature as a hash map key to group anagrams together in direct object references.

        Time Complexity: O(n * m) - Where n is the number of strings and m is the maximum string length. We traverse each character of every string exactly once.
        Space Complexity: O(n * m) - The hash map stores all n strings of max length m. The signature itself takes O(1) space since it is always strictly 26 integers.
        """
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                ind = ord(c) - ord("a")
                count[ind] += 1

            signature = tuple(count)
            groups[signature].append(s)

        return list(groups.values())
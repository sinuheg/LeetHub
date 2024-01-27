class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for char in s:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
        for char in t:
            if char not in freq:
                return False
            if freq[char]==1:
                del freq[char]
            else:
                freq[char] -= 1
        if freq:
            return False
        else:
            return True
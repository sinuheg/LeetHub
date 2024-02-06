class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        hs = set()
        hs.add(s[0])
        left = 0
        right = 1
        maxlen = 1
        while right < len(s):
            incoming = s[right]
            if incoming in hs:
                while left < right and s[left] != incoming:
                    hs.remove(s[left])
                    left += 1
                left += 1
            else:
                hs.add(incoming)
                newlen = right - left + 1
                maxlen = max(newlen, maxlen)
            right += 1
        return maxlen
        
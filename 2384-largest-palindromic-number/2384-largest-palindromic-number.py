from collections import deque
class Solution:
    def largestPalindromic(self, num):
        digit_freq = {}
        for digit in num:
            if digit not in digit_freq:
                digit_freq[digit] = 0
            digit_freq[digit] += 1
        odd = -1
        result = deque()
        for digit in range(9,-1,-1):
            if str(digit) in digit_freq:
                freq = digit_freq[str(digit)]
                if freq >= 2:
                    for _ in range(freq//2):
                        freq -= 2
                        result.append(str(digit))
                if freq == 1 :
                    if odd == -1:
                        odd = str(digit)
        while result and result[0] == '0':
            result.popleft()
        half_len = len(result)
        if odd != -1:
            result.append(odd)
        for i in range(half_len-1, -1, -1):
            result.append(result[i])
        if not result:
            result.append('0')
        return ''.join(result)
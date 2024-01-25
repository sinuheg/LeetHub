class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(left,right):
            if left >= right:
                return
            while left < right:
                aux = s_array[left]
                s_array[left] = s_array[right]
                s_array[right] = aux
                left += 1
                right -= 1
        i = 0
        s_array = []
        last_word_ends = -1
        while i < len(s):
            while i < len(s) and s[i] == ' ':
                i += 1
            if last_word_ends > 0 and i < len(s) and s[i] != ' ':
                s_array.append(' ')
            while i < len(s) and s[i] != ' ':
                s_array.append(s[i])
                i += 1
            reverse(last_word_ends+1, len(s_array)-1)
            last_word_ends = len(s_array)
        reverse(0, len(s_array)-1)
        return ''.join(s_array)



class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s)-1
        vowels = 'aeiou'
        sarray = list(s)
        while right >= left:
            while left < right and sarray[left].lower() not in vowels:
                left += 1
            while right > left and sarray[right].lower() not in vowels:
                right -= 1
            if left <= right:
                aux = sarray[left]
                sarray[left] = sarray[right]
                sarray[right] = aux
                left += 1
                right -= 1
        return ''.join(sarray)
            
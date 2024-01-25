class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def is_divisible(string1, string2):
            if len(string1) > len(string2):
                return False
            if len(string2) % len(string1) != 0:
                return False
            for i in range(len(string2)):
                j = i % len(string1)
                if string2[i] != string1[j]:
                    return False
            return True
        min_common = ''
        current = []
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                current.append(str1[i])
            else:
                return ''
            if is_divisible(current, str1) and is_divisible(current, str2):
                min_common = ''.join(current)
        return ''.join(min_common)
        
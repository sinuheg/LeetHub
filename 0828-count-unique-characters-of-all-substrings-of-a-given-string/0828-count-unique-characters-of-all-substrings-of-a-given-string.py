class Solution:
    def uniqueLetterString(self, s: str) -> int:
        prev = [-1] * len(s)
        nex = [len(s)] * len(s)
        index = {}
        for i, c in enumerate(s):
            if c in index:
                prev[i] = index[c]    
            index[c] = i
        index = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] in index:
                nex[i] = index[s[i]]
            index[s[i]] = i
        uniques = 0
        for i in range(len(s)):
            uniques += (nex[i] - i) * (i - prev[i])
        return uniques
        # def calculate_uniques(left, right):
        #     nonlocal total
        #     uniques = 0
        #     for i in range(left,right+1):
        #         char = s[i]
        #         counter[char]+= 1
        #         if counter[char] == 1:
        #             uniques += 1
        #         elif counter[char] == 2:
        #             uniques -= 1
        #         total += uniques
        #     for i in range(left, right+1):
        #         char = s[i]
        #         counter[char]-=1
        #         if counter[char] == 1:
        #             uniques += 1
        #         elif counter[char] == 0:
        #             uniques -= 1
        #         total += uniques

        # counter = {char: 0 for char in ascii_uppercase}
        # left = 0
        # right = len(s)-1
        # total = 0
        # while left <= right:
        #     calculate_uniques(left,right)
        #     left+=1
        #     right-=1
        # return total


        # counter = {}
        # left = 0
        # total = 0
        # while left < len(s):
        #     right = left
        #     counter = {}
        #     uniques = 0
        #     while right < len(s):
        #         char_to_add = s[right]
        #         if char_to_add not in counter:
        #             counter[char_to_add] = 1
        #             uniques += 1
        #         else:
        #             counter[char_to_add] += 1
        #             if counter[char_to_add] == 2:
        #                 uniques -= 1
        #         total += uniques
        #         right += 1
        #     left += 1
        # return total

        # def count_unique_chars(string):
        #     unique = set()
        #     seen = set()
        #     for char in string:
        #         if char in unique:
        #             unique.remove(char)
        #             seen.add(char)
        #         else:
        #             if char not in seen:
        #                 unique.add(char)
        #             else:
        #                 seen.add(char)
        #     return len(unique)
                
        # def get_substrings(start):
        #     if start >= len(s):
        #         return []
        #     substrings = get_substrings(start+1)
        #     for i in range(start, len(s)):
        #         substrings.append(s[start:i+1])
        #     return substrings
        # substrings = get_substrings(0)
        # sum = 0
        # for substring in substrings:
        #     sum += count_unique_chars(substring)
        # return sum
        
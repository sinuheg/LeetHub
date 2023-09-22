'''
[100,4,200,1,3,2]
               ^
{4, 3 , 2, 1}
max 4


1 2 3 4 78 98 54 21 7 8 9 10 11
                              ^
{1, 2, 3, 4, 7, 8, 9 ,10, 11}
curr = 5
max = 4

find window
    finds upward and downwards in original set
    if found adds to used numbers
    count increases for each number added
    updates max

for each element
    if not in used
        find window
    if used
        go to next
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        originals = set(nums)
        used = set()
        max_seq = 0
        for num in nums:
            if num not in used:
                end = num
                while end + 1 in originals:
                    end += 1
                    used.add(end)
                start = num
                while start - 1 in originals:
                    start -= 1
                    used.add(start)
                window = end - start + 1
                if window > 1:
                    used.add(num)
                max_seq = max(window, max_seq)
        return max_seq
        
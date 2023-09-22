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
        
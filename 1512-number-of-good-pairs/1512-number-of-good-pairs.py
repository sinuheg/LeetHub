class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        pairs = 0
        for _,count in counter.items():
            pairs += count*(count-1)//2
        return pairs
        
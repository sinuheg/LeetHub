import heapq
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        arr = []
        while nums:
            alice_num = heapq.heappop(nums)
            bob_num = heapq.heappop(nums)
            arr.append(bob_num)
            arr.append(alice_num)
        return arr
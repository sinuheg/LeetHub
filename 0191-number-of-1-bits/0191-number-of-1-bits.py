class Solution:
    def hammingWeight(self, n: int) -> int:
        filter = 1
        counter = 0
        for _ in range(32):
            if n & filter == filter:
                counter += 1
            filter = filter << 1
        return counter
        
                
        
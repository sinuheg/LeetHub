'''
[                   0  0]
[73,74,75,71,69,72,76,73]
                ^
[73]
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for i,temperature in enumerate(temperatures):
            if not stack:
                stack.append((i,temperature))
            else:
                while stack and temperature > stack[-1][1]:
                    j,_ = stack.pop()
                    result[j] = i - j
                stack.append((i,temperature))
        return result
                    

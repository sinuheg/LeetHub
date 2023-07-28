"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

Pseudo code:
iterate matrix row col
if find a 1
    add island count
    flip island to -1

return count

flip the island
    check boundaries
    check if is not 1 return
    flip current to -1
    check up
    check down
    check left
    check right
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    island_count += 1
                    self.flip_island(grid,row,col)
        return island_count
    
    def flip_island(self, grid, row, col):
        if row < 0 or row >= len(grid):
            return
        if col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] != "1":
            return
        grid[row][col] = "-1"
        self.flip_island(grid, row-1, col)
        self.flip_island(grid, row+1, col)
        self.flip_island(grid, row, col-1)
        self.flip_island(grid, row, col+1)
        
sol = Solution()
# Test 1:
# Input
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# Expected Output: 1
print(sol.numIslands(grid))



# Test 2:

# Input: 
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# Expected Output: 3
print(sol.numIslands(grid))
"""
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
        
import heapq
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            for i,num in enumerate(row):
                row[i] = -num
            heapq.heapify(row)
        result = 0
        while True:
            max_cell = 0
            rows_with_cells = len(grid)
            for row in grid:
                if not row:
                    rows_with_cells-=1
                else:
                    popped = heapq.heappop(row)*-1
                    max_cell = max(max_cell, popped)
            result += max_cell
            if rows_with_cells == 0:
                break
        return result

        
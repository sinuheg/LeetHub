class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search_rows():
            start = 0
            end = len(matrix)-1
            while start <= end:
                mid = start + ((end - start) // 2)
                min_row = matrix[mid][0]
                max_row = matrix[mid][len(matrix[mid])-1]
                if  min_row <= target and target <= max_row:
                    return matrix[mid]
                elif target > max_row:
                    start = mid + 1
                else:
                    end = mid - 1
            return []
        
        def search_in_row(row):
            start = 0
            end = len(row) - 1
            while start <= end:
                mid = start + ((end - start) // 2)
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return False
        selected_row = search_rows()
        return search_in_row(selected_row)
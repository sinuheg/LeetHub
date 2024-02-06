class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def get_position_for(edge, i, j, n):
            if edge == 'top':
                return i+j, i
            elif edge == 'right':
                return n - i -1, i+j
            elif edge == 'bottom':
                return n - i - j - 1, n - i -1
            elif edge == 'left':
                return i, n -i -j - 1

        if len(matrix) < 2:
            return
        n = len(matrix)
        for i in range(n//2):
            for j in range(n-2*i-1):
                col_to,row_to = get_position_for('top', i, j, n)
                temp = matrix[row_to][col_to]
                # left to top
                col_from, row_from = get_position_for('left', i, j, n)
                matrix[row_to][col_to] = matrix[row_from][col_from]
                # bottom to left
                col_to = col_from
                row_to = row_from
                col_from, row_from = get_position_for('bottom', i, j, n)
                matrix[row_to][col_to] = matrix[row_from][col_from]
                # right to bottom
                col_to = col_from
                row_to = row_from
                col_from, row_from = get_position_for('right', i, j, n)
                matrix[row_to][col_to] = matrix[row_from][col_from]
                # temp to right
                col_to = col_from
                row_to = row_from
                matrix[row_to][col_to] = temp
        
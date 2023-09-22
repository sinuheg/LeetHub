class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_sets = []
        row_sets = []
        sqr_sets = []
        for _ in range(9):
            col_sets.append(set())
            row_sets.append(set())
            sqr_sets.append(set())

        row = 0
        while row < 9:
            col = 0
            while col < 9:
                val = board[row][col]
                if val != '.':
                    if val in col_sets[col]:
                        return False
                    else:
                        col_sets[col].add(val)
                    if val in row_sets[row]:
                        return False
                    else:
                        row_sets[row].add(val)
                    sqr = (row // 3) * 3 + (col // 3)
                    if val in sqr_sets[sqr]:
                        return False
                    else:
                        sqr_sets[sqr].add(val)
                col += 1
            row += 1
        return True
        
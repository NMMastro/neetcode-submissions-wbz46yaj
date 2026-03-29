class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()

       # Check horizontal lines
        for row in range(9):
            for column in range(9):
                item = board[row][column]

                if item == ".":
                    continue
                elif item in s:
                    return False

                s.add(item)

            s.clear()

        # Check vertical lines
        for row in range(9):
            for column in range(9):
                item = board[column][row]

                if item == ".":
                    continue
                elif item in s:
                    return False

                s.add(item)

            s.clear()


        # Check grid
        for row_square in range(3):
            for col_square in range(3):

                for row in range(row_square * 3, row_square * 3 + 3):
                    for col in range(col_square * 3, col_square * 3 + 3):
                        item = board[row][col]

                        if item == ".":
                            continue
                        elif item in s:
                            return False

                        s.add(item)

                s.clear()

        
        return True

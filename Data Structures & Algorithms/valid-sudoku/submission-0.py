class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = 9
        count = {}
        # Checking each row for duplicates
        for row in board:
            count.clear()
            for num in row:
                if num != ".":
                    count[num] = count.get(num, 0) + 1
                    if count[num] > 1:
                        print("Failed row: ", count)
                        return False
        count.clear()

        # Checking each column for duplicates
        for column in range(n):
            count.clear()
            for row in range(n):
                if board[row][column] != ".":
                    count[board[row][column]] = count.get(board[row][column], 0) + 1
                    if count[board[row][column]] > 1:
                        print('duplicate in column',count)
                        return False
        #print(count)
        count.clear()

        # Checking each box for duplicates
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                count = {}

                for r in range(row_start, row_start + 3):
                    for c in range(col_start, col_start + 3):
                        num = board[r][c]

                        if num != ".":
                            count[num] = count.get(num, 0) + 1

                            if count[num] > 1:
                                return False
        print(count)
        return True

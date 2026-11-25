class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = {(kind, i): set() for kind in ("row", "col", "box") for i in range(1, 10)}
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen[("row", i + 1)]:
                    return False
                elif board[i][j] in seen[("col", j + 1)]:
                    return False
                if i < 3:
                    if j < 3: boxN = 1
                    elif 3 <= j < 6: boxN = 2
                    elif j >= 6: boxN = 3
                elif 3 <= i < 6:
                    if j < 3: boxN = 4
                    elif 3 <= j < 6: boxN = 5
                    elif j >= 6: boxN = 6
                elif i >= 6:
                    if j < 3: boxN = 7
                    elif 3 <= j < 6: boxN = 8
                    elif j >= 6: boxN = 9
                if board[i][j] in seen[("box", boxN)]:
                    return False
                seen[("row", i + 1)].add(board[i][j])
                seen[("col", j + 1)].add(board[i][j])
                seen[("box", boxN)].add(board[i][j])

        return True
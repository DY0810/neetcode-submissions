class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = {(kind, i): set() for kind in ("row", "col", "box") for i in range(1, 10)}
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == ".":
                    continue
                if curr in seen[("row", i + 1)]:
                    return False
                elif curr in seen[("col", j + 1)]:
                    return False
                boxN = ((i // 3) * 3 + j // 3) + 1
                if curr in seen[("box", boxN)]:
                    return False
                seen[("row", i + 1)].add(curr)
                seen[("col", j + 1)].add(curr)
                seen[("box", boxN)].add(curr)

        return True
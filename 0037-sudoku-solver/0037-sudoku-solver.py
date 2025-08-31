class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [[0] * 10 for _ in range(9)]
        cols = [[0] * 10 for _ in range(9)]
        boxes = [[0] * 10 for _ in range(9)]
        empties = []

        # Pre-fill
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empties.append((i, j))
                else:
                    d = int(board[i][j])
                    rows[i][d] = cols[j][d] = boxes[(i // 3) * 3 + j // 3][d] = 1

        def backtrack(k):
            if k == len(empties):
                return True
            i, j = empties[k]
            b = (i // 3) * 3 + j // 3
            for d in range(1, 10):
                if not rows[i][d] and not cols[j][d] and not boxes[b][d]:
                    board[i][j] = str(d)
                    rows[i][d] = cols[j][d] = boxes[b][d] = 1
                    if backtrack(k + 1):
                        return True
                    board[i][j] = "."
                    rows[i][d] = cols[j][d] = boxes[b][d] = 0
            return False

        backtrack(0)

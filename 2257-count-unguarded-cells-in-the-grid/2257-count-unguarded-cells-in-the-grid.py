class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [[0]*n for _ in range(m)]
        for r, c in walls: grid[r][c] = -1
        for r, c in guards: grid[r][c] = 1
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        for r, c in guards:
            for dr, dc in dirs:
                x, y = r+dr, c+dc
                while 0 <= x < m and 0 <= y < n and grid[x][y] != -1 and grid[x][y] != 1:
                    if grid[x][y] == 0: grid[x][y] = 2
                    x += dr; y += dc
        return sum(v == 0 for row in grid for v in row)

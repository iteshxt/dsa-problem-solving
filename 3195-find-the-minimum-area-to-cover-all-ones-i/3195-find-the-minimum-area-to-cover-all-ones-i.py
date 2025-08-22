class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        top, left = rows, cols
        bottom, right = -1, -1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    top = min(top, r)
                    left = min(left, c)
                    bottom = max(bottom, r)
                    right = max(right, c)

        if bottom == -1:  # no 1s in grid
            return 0
        
        return (bottom - top + 1) * (right - left + 1)

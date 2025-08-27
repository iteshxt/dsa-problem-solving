class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        # DP arrays for both diagonal directions
        downRight = [[0] * m for _ in range(n)]
        downLeft = [[0] * m for _ in range(n)]
        
        # Fill bottom-up
        for i in range(n-1, -1, -1):
            for j in range(m):
                if grid[i][j] == 1:
                    downRight[i][j] = 1 + (downRight[i+1][j+1] if i+1 < n and j+1 < m else 0)
                    downLeft[i][j]  = 1 + (downLeft[i+1][j-1] if i+1 < n and j-1 >= 0 else 0)
        
        # Check max V-length
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(ans, min(downRight[i][j], downLeft[i][j]))
        return ans
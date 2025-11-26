from typing import List

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[i][j][r]: number of ways to reach (i, j) with sum % k = r
        dp = [[[0] * k for _ in range(n)] for __ in range(m)]
        
        first_rem = grid[0][0] % k
        dp[0][0][first_rem] = 1
        
        for i in range(m):
            for j in range(n):
                val = grid[i][j] % k
                if i == 0 and j == 0:
                    continue  # already initialized
                
                # from top
                if i > 0:
                    for r in range(k):
                        if dp[i-1][j][r]:
                            new_r = (r + val) % k
                            dp[i][j][new_r] = (dp[i][j][new_r] + dp[i-1][j][r]) % MOD
                
                # from left
                if j > 0:
                    for r in range(k):
                        if dp[i][j-1][r]:
                            new_r = (r + val) % k
                            dp[i][j][new_r] = (dp[i][j][new_r] + dp[i][j-1][r]) % MOD
        
        return dp[m-1][n-1][0]

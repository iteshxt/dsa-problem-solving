class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 1_000_000_007
        
        # Step 1: Precompute powers <= n
        powers = []
        base = 1
        while (p := base ** x) <= n:
            powers.append(p)
            base += 1
        
        # Step 2: 1D DP - dp[t] = number of ways to make sum 't'
        dp = [0] * (n + 1)
        dp[0] = 1  # one way to make 0 sum
        
        for p in powers:
            # iterate backwards to ensure each power is used at most once
            for t in range(n, p - 1, -1):
                dp[t] = (dp[t] + dp[t - p]) % MOD
        
        return dp[n]
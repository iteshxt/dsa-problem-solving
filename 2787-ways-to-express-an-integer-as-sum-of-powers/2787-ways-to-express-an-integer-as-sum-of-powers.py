class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 1_000_000_007
        
        # Precompute all powers <= n
        powers = []
        num = 1
        while (p := num ** x) <= n:
            powers.append(p)
            num += 1
        
        from functools import lru_cache
        
        @lru_cache(None)
        def dfs(index, target):
            """
            index: position in 'powers' list
            target: remaining sum we need to form
            Returns number of ways to form 'target' using powers[index:]
            """
            if target == 0:
                return 1  # found a valid combination
            if index == len(powers) or target < 0:
                return 0  # no valid combination
            
            # Option 1: take this power
            take = dfs(index + 1, target - powers[index])
            # Option 2: skip this power
            skip = dfs(index + 1, target)
            
            return (take + skip) % MOD
        
        return dfs(0, n)
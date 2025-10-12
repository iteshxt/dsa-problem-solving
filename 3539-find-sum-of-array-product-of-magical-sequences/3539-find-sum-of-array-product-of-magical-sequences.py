class Solution:
    def magicalSum(self, m: int, k: int, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        dp = [0] * (1 << n)
        for i in range(n):
            dp[1 << i] = nums[i]
        for _ in range(m - 1):
            new_dp = [0] * (1 << n)
            for mask in range(1 << n):
                if dp[mask] == 0:
                    continue
                for i in range(n):
                    new_mask = mask + (1 << i)
                    if new_mask < (1 << n):
                        new_dp[new_mask] = (new_dp[new_mask] + dp[mask] * nums[i]) % MOD
            dp = new_dp
        ans = 0
        for mask in range(1 << n):
            if bin(mask).count('1') == k:
                ans = (ans + dp[mask]) % MOD
        return ans

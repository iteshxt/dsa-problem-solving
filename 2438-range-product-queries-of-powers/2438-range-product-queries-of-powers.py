MOD = 10**9 + 7

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        powers = []
        bit = 0
        while n > 0:
            if n & 1:
                powers.append(pow(2, bit, MOD))
            bit += 1
            n >>= 1
        prefix = [1]
        for p in powers:
            prefix.append((prefix[-1] * p) % MOD)
        ans = []
        for l, r in queries:
            ans.append((prefix[r+1] * pow(prefix[l], MOD-2, MOD)) % MOD)
        return ans
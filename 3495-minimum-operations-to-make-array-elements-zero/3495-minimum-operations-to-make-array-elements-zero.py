class Solution:
    def minOperations(self, queries: list[list[int]]) -> int:
        def getOperations(n: int) -> int:
            res = 0
            ops = 0
            power = 1
            while power <= n:
                left = power
                right = min(n, power * 4 - 1)
                ops += 1
                res += (right - left + 1) * ops
                power *= 4
            return res

        total = 0
        for l, r in queries:
            total += (getOperations(r) - getOperations(l - 1) + 1) // 2
        return total

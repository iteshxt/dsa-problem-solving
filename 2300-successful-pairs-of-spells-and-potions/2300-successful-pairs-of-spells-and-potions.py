from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        n = len(potions)
        res = []
        for s in spells:
            target = (success + s - 1) // s
            idx = bisect_left(potions, target)
            res.append(n - idx)
        return res

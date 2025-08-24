class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1, count2 = Counter(basket1), Counter(basket2)
        total = count1 + count2   # combined count of all fruits

        # 1. Check feasibility
        for fruit in total:
            if total[fruit] % 2 != 0:
                return -1  # odd occurrence, impossible
        
        # 2. Find excess fruits
        extra = []
        for fruit in total:
            diff = count1[fruit] - count2[fruit]
            if diff > 0:
                extra.extend([fruit] * (diff // 2))  # extra in basket1
            elif diff < 0:
                extra.extend([fruit] * (-diff // 2)) # extra in basket2
        
        # Only need to fix half (swap pairs)
        extra.sort()
        min_global = min(total.keys())
        
        res = 0
        # Only first half of extra needs swapping (other half matches them)
        for i in range(len(extra)//2):
            res += min(extra[i], 2 * min_global)
        
        return res
from bisect import bisect_right
from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [1]*n
        dry_days = []
        last_rain = {}
        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(i)
            else:
                ans[i] = -1
                if lake in last_rain:
                    pos = bisect_right(dry_days, last_rain[lake])
                    if pos == len(dry_days):
                        return []
                    dry_index = dry_days.pop(pos)
                    ans[dry_index] = lake
                last_rain[lake] = i
        return ans

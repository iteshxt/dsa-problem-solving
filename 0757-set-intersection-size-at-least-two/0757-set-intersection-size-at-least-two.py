class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        chosen = []
        ans = 0

        for start, end in intervals:
            cnt = 0
            for x in reversed(chosen[-2:]):
                if start <= x <= end:
                    cnt += 1

            if cnt == 0:
                chosen.append(end - 1)
                chosen.append(end)
                ans += 2
            elif cnt == 1:
                chosen.append(end)
                ans += 1

        return ans

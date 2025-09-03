class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                valid = True
                for k in range(n):
                    if k == i or k == j:
                        continue
                    x3, y3 = points[k]

                    # collinearity check
                    if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
                        # inside segment?
                        if min(x1, x2) <= x3 <= max(x1, x2) and \
                           min(y1, y2) <= y3 <= max(y1, y2):
                            valid = False
                            break
                if valid:
                    ans += 1
        return ans

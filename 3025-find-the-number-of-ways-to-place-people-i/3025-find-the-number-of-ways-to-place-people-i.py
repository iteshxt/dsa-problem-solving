class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        ans = 0
        n = len(points)
        for i in range(n):
            yi = points[i][1]
            maxY = -10**9
            for j in range(i + 1, n):
                yj = points[j][1]
                if yj <= yi and yj > maxY:
                    ans += 1
                    maxY = yj
        return ans

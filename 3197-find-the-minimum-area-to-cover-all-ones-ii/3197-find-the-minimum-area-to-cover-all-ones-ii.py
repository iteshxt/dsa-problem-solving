class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def min_area(si, ei, sj, ej):
            x1 = float('inf')
            y1 = float('inf')
            x2 = y2 = -1
            for i in range(si, ei + 1):
                for j in range(sj, ej + 1):
                    if grid[i][j] == 1:
                        x1 = min(x1, i)
                        y1 = min(y1, j)
                        x2 = max(x2, i)
                        y2 = max(y2, j)
            return 0 if x2 < 0 else (x2 - x1 + 1) * (y2 - y1 + 1)

        ans = m * n  # initialize with full area as worst case

        # L-shaped splits (4 variants)
        for i in range(m - 1):
            top = min_area(0, i, 0, n - 1)
            bottom_remaining = lambda sj, ej: min_area(i + 1, m - 1, sj, ej)
            for j in range(n - 1):
                # Split bottom into left and right
                left_part = bottom_remaining(0, j)
                right_part = bottom_remaining(j + 1, n - 1)
                ans = min(ans, top + left_part + right_part)

        for i in range(1, m):
            bottom = min_area(i, m - 1, 0, n - 1)
            top_remaining = lambda sj, ej: min_area(0, i - 1, sj, ej)
            for j in range(n - 1):
                left_part = top_remaining(0, j)
                right_part = top_remaining(j + 1, n - 1)
                ans = min(ans, bottom + left_part + right_part)

        for j in range(n - 1):
            left = min_area(0, m - 1, 0, j)
            right_remaining = lambda si, ei: min_area(si, ei, j + 1, n - 1)
            for i in range(m - 1):
                top_part = right_remaining(0, i)
                bottom_part = right_remaining(i + 1, m - 1)
                ans = min(ans, left + top_part + bottom_part)

        for j in range(1, n):
            right = min_area(0, m - 1, j, n - 1)
            left_remaining = lambda si, ei: min_area(si, ei, 0, j - 1)
            for i in range(m - 1):
                top_part = left_remaining(0, i)
                bottom_part = left_remaining(i + 1, m - 1)
                ans = min(ans, right + top_part + bottom_part)

        # Horizontal triplet stripes
        for i1 in range(m - 2):
            for i2 in range(i1 + 1, m - 1):
                a = min_area(0, i1, 0, n - 1)
                b = min_area(i1 + 1, i2, 0, n - 1)
                c = min_area(i2 + 1, m - 1, 0, n - 1)
                ans = min(ans, a + b + c)

        # Vertical triplet stripes
        for j1 in range(n - 2):
            for j2 in range(j1 + 1, n - 1):
                a = min_area(0, m - 1, 0, j1)
                b = min_area(0, m - 1, j1 + 1, j2)
                c = min_area(0, m - 1, j2 + 1, n - 1)
                ans = min(ans, a + b + c)

        return ans

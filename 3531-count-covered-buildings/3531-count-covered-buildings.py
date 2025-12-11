from typing import List
import math
from collections import defaultdict

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # store min/max y for each row x
        min_y = defaultdict(lambda: math.inf)
        max_y = defaultdict(lambda: -math.inf)
        # store min/max x for each col y
        min_x = defaultdict(lambda: math.inf)
        max_x = defaultdict(lambda: -math.inf)

        # first pass: fill extremes
        for x, y in buildings:
            if y < min_y[x]: min_y[x] = y
            if y > max_y[x]: max_y[x] = y
            if x < min_x[y]: min_x[y] = x
            if x > max_x[y]: max_x[y] = x

        # second pass: count covered
        covered = 0
        for x, y in buildings:
            if min_y[x] < y < max_y[x] and min_x[y] < x < max_x[y]:
                covered += 1

        return covered

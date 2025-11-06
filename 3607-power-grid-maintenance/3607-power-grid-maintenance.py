from collections import defaultdict
from sortedcontainers import SortedList

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[rb] = ra

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu = DSU(c + 1)
        for u, v in connections:
            dsu.union(u, v)
        comp = defaultdict(SortedList)
        for i in range(1, c + 1):
            comp[dsu.find(i)].add(i)
        online = [True] * (c + 1)
        res = []
        for op, x in queries:
            root = dsu.find(x)
            if op == 1:
                if online[x]:
                    res.append(x)
                else:
                    res.append(comp[root][0] if comp[root] else -1)
            else:
                if online[x]:
                    online[x] = False
                    comp[root].remove(x)
        return res


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        m = max(len(v1), len(v2))
        v1 += [0]*(m - len(v1))
        v2 += [0]*(m - len(v2))
        return (v1 > v2) - (v1 < v2)

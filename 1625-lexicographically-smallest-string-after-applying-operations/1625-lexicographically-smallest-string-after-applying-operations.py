class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = set()
        queue = deque([s])
        ans = s
        while queue:
            curr = queue.popleft()
            if curr in seen:
                continue
            seen.add(curr)
            ans = min(ans, curr)
            added = list(curr)
            for i in range(1, len(s), 2):
                added[i] = str((int(added[i]) + a) % 10)
            added = ''.join(added)
            rotated = curr[-b:] + curr[:-b]
            queue.extend([added, rotated])
        return ans

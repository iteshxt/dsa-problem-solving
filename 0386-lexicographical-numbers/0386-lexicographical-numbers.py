class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(curr):
            if curr > n:
                return
            res.append(curr)
            for i in range(10):
                nxt = curr * 10 + i
                if nxt > n:
                    break
                dfs(nxt)

        for i in range(1, 10):
            dfs(i)

        return res
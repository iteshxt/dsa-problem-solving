class Solution:
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])
        sorted_pairs = [False] * (n - 1)
        deletions = 0

        for col in range(m):
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][col] > strs[i + 1][col]:
                    deletions += 1
                    break
            else:
                for i in range(n - 1):
                    if not sorted_pairs[i] and strs[i][col] < strs[i + 1][col]:
                        sorted_pairs[i] = True

        return deletions

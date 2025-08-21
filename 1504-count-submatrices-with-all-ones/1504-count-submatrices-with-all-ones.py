class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        # Step 1: compute heights of consecutive ones in each column
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and i > 0:
                    mat[i][j] += mat[i-1][j]

        # Step 2: count submatrices using each row as base
        for i in range(m):
            stack = []
            count = [0] * n
            for j in range(n):
                while stack and mat[i][stack[-1]] >= mat[i][j]:
                    stack.pop()
                if stack:
                    prev_index = stack[-1]
                    count[j] = count[prev_index] + mat[i][j] * (j - prev_index)
                else:
                    count[j] = mat[i][j] * (j + 1)
                res += count[j]
                stack.append(j)
        return res

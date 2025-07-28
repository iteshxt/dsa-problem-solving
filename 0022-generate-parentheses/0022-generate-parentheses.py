class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, sol = [], []

        def backtrack(openB, closeB):
            
            # conditions 
            # add "(" if open < n
            # add ")" if closed < open
            # valid if open == closed == n || sol == 2n

            if len(sol) == 2*n:
                ans.append("".join(sol))
            
            if openB < n:
                sol.append("(")
                backtrack(openB + 1, closeB)
                sol.pop()
            
            if closeB < openB:
                sol.append(")")
                backtrack(openB, closeB +1)
                sol.pop()

        backtrack(0,0)

        return ans

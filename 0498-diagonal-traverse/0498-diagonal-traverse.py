class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat: 
            return []
        
        m, n = len(mat), len(mat[0])
        res = []
        
        for d in range(m + n - 1):  # total diagonals
            temp = []
            
            # figure out starting point
            r = 0 if d < n else d - n + 1
            c = d if d < n else n - 1
            
            # collect elements on this diagonal
            while r < m and c >= 0:
                temp.append(mat[r][c])
                r += 1
                c -= 1
            
            # reverse on even diagonals
            if d % 2 == 0:
                res.extend(temp[::-1])
            else:
                res.extend(temp)
        
        return res

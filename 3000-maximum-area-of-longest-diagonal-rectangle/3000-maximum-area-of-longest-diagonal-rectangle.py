class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = 0
        max_area = 0
        
        for w, h in dimensions:
            diag = w * w + h * h   # squared diagonal
            area = w * h
            
            if diag > max_diag or (diag == max_diag and area > max_area):
                max_diag = diag
                max_area = area
                
        return max_area
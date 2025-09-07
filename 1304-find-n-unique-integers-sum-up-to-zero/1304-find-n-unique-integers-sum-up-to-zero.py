class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        
        # Add pairs
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)
        
        # If n is odd, add 0
        if n % 2 != 0:
            result.append(0)
            
        return result

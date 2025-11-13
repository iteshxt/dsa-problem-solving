class Solution:
    def maxOperations(self, s: str) -> int:
        zeros = 0
        ops = 0
        
        for ch in reversed(s):
            if ch == '0':
                zeros += 1
            else:  
                ops += zeros
        
        return ops

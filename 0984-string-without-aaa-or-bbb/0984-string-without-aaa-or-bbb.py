class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        result = []
        
        while A > 0 or B > 0:
            if len(result) >= 2 and result[-1] == result[-2]:
                # If last two are the same, add the opposite letter
                if result[-1] == 'a':
                    result.append('b')
                    B -= 1
                else:
                    result.append('a')
                    A -= 1
            else:
                # Otherwise, add the letter with the greater remaining count
                if A >= B:
                    result.append('a')
                    A -= 1
                else:
                    result.append('b')
                    B -= 1
        
        return ''.join(result)

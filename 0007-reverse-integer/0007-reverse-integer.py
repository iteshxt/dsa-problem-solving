class Solution:
    def reverse(self, x: int) -> int:
        
        if str(x)[0] == "-":
            s_x = str(x)[1::]

            s_x = s_x[::-1]

            s_x = int(s_x)
            s_x = -s_x
        else:
            s_x = str(x)
            s_x = s_x[::-1]
        
        sol = int(s_x)

        if sol > 2**31-1 or sol < -2**31:
            return 0

        return sol
    

        
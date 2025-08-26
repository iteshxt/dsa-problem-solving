class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1
        count = 9
        start = 1
        
        # Find the length group
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10
        
        # Find the target number
        start += (n - 1) // length
        s = str(start)
        
        # Return the correct digit
        return int(s[(n - 1) % length])

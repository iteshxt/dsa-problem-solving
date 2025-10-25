class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        
        total = weeks * 28 + 7 * (weeks * (weeks - 1)) // 2
        
        start = weeks + 1
        total += days * start + (days * (days - 1)) // 2
        
        return total

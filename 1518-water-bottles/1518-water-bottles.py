class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            new_full = empty // numExchange
            drank += new_full
            empty = empty % numExchange + new_full
            
        return drank

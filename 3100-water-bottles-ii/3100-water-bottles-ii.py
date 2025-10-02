class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles
        empty = numBottles
        exchange_cost = numExchange

        while empty >= exchange_cost:
            # Perform one exchange
            empty -= exchange_cost
            drank += 1
            empty += 1  # the new bottle, once drunk, becomes empty
            exchange_cost += 1

        return drank

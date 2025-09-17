from typing import List
import heapq

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.info = {}
        self.heaps = {}
        for f,c,r in zip(foods,cuisines,ratings):
            self.info[f] = (c,r)
            self.heaps.setdefault(c, [])
            heapq.heappush(self.heaps[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        c, _ = self.info[food]
        self.info[food] = (c, newRating)
        heapq.heappush(self.heaps[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        h = self.heaps[cuisine]
        while h:
            negr, f = h[0]
            if self.info[f][1] == -negr:
                return f
            heapq.heappop(h)
        return ""

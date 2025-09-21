import heapq
from collections import defaultdict

class MovieRentingSystem:
    def __init__(self, n: int, entries: list[list[int]]):
        self.price = {}
        self.available = defaultdict(list)
        self.rented = []
        self.is_rented = {}
        for shop, movie, cost in entries:
            self.price[(shop, movie)] = cost
            heapq.heappush(self.available[movie], (cost, shop))
            self.is_rented[(shop, movie)] = False

    def search(self, movie: int) -> list[int]:
        res = []
        heap = self.available[movie]
        i = 0
        while i < len(heap) and len(res) < 5:
            cost, shop = heap[i]
            if not self.is_rented[(shop, movie)]:
                res.append(shop)
            i += 1
        return res

    def rent(self, shop: int, movie: int) -> None:
        self.is_rented[(shop, movie)] = True
        heapq.heappush(self.rented, (self.price[(shop, movie)], shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.is_rented[(shop, movie)] = False
        heapq.heappush(self.available[movie], (self.price[(shop, movie)], shop))

    def report(self) -> list[list[int]]:
        res = []
        while self.rented and len(res) < 5:
            cost, shop, movie = self.rented[0]
            if self.is_rented[(shop, movie)]:
                res.append([shop, movie])
                heapq.heappop(self.rented)
                heapq.heappush(self.rented, (cost, shop, movie))
                break
            heapq.heappop(self.rented)
        j = 0
        while j < len(self.rented) and len(res) < 5:
            cost, shop, movie = self.rented[j]
            if self.is_rented[(shop, movie)]:
                res.append([shop, movie])
            j += 1
        return res

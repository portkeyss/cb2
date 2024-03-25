from sortedcontainers import SortedList
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.unrented = defaultdict(SortedList)
        self.prices = dict() # map (shop,movie) to it's price
        self.rented = SortedList()
        for shop, movie, price in entries:
            self.unrented[movie].add((price,shop))
            self.prices[(shop,movie)] = price
        

    def search(self, movie: int) -> List[int]:
        return [x for _,x in self.unrented[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.prices[(shop,movie)]
        self.unrented[movie].remove((price,shop))
        self.rented.add((price,shop,movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.prices[(shop,movie)]
        self.rented.remove((price,shop,movie))
        self.unrented[movie].add((price,shop))

    def report(self) -> List[List[int]]:
        return [[shop,movie] for _,shop,movie in self.rented[:5]]
        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
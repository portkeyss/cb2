class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = set()
        for path in paths:
            cities.add(path[0])
            cities.add(path[1])
        for path in paths:
            cities.discard(path[0])
        return cities.pop()
class Solution:
    def countPoints(self, rings: str) -> int:
        colors = [set() for _ in range(10)]
        for i in range(0, len(rings), 2):
            colors[int(rings[i+1])].add(rings[i])
        return sum(len(color)==3 for color in colors)
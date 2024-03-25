class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        i, j = 0, n-1
        while colors[i]==colors[-1]:
            i += 1
        while colors[j]==colors[0]:
            j -= 1
        return max(n-1-i, j)
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        #from the right, construct a increasing subsequence from height
        h = 0
        res = []
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > h:
                res.append(i)
                h = heights[i]
            i -= 1
        return res[::-1]
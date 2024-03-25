class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        A = sorted(zip(plantTime,growTime),key=lambda x:-x[1])
        res = 0
        curTime = 0
        for p,g in A:
            curTime += p
            res = max(res,curTime+g)
        return res
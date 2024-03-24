class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        m = 0
        for a in arr:
            if a%2==1:
                m += 1
                if m==3: return True
            else:
                m = 0
        return False
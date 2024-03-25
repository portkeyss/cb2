class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n%3 in [0,1]: n//=3
            else: return False
        return True
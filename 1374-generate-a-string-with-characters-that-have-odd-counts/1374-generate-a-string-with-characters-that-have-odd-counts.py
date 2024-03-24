class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2==0: return "".join(["a"]*(n-1)+["b"])
        else: return "".join(["a"]*n)
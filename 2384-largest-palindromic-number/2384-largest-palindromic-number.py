class Solution:
    def largestPalindromic(self, num: str) -> str:
        n = len(num)
        counter = Counter(num)
        if counter["0"]==n: return "0"
        A = []
        center = "" 
        for i in range(10):
            x = counter[str(i)]
            if x==0: continue
            if x>1:
                A += [str(i)]*(x//2)
            if x%2==1:
                center = str(i)
        if A and A[-1]=="0": return center
        return "".join(A[::-1]+[center]+A)
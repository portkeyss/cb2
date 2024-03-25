class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        for i in range(n): # i is the ending index of the first number
            a = int(s[:i+1])
            if a==0: continue
            j = i+1
            while j < n: #j is the current number's starting index
                if a==1:
                    if int(s[j:])==0: return True
                    else: break
                k = j #k is the current number's ending index
                b = 0
                while k<n and 10*b+int(s[k])<a-1:
                    b = 10*b+int(s[k])
                    k += 1
                if k<n and 10*b+int(s[k])==a-1: 
                    if k+1==n: return True
                    a -= 1
                    j = k+1
                else:
                    break
        return False
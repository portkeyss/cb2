class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        S = [s1, s2]
        
        @lru_cache(None)
        def getVals(strIdx, i):
            s = S[strIdx]
            j = i
            while j<len(s) and s[j].isnumeric(): j+=1
            vals = []
            if j==i+1: vals = [int(s[i])]
            elif j==i+2: vals = [int(s[i:i+2]), int(s[i])+int(s[i+1])]
            else: vals = [int(s[i:i+3]), int(s[i:i+1])+int(s[i+1:i+3]), int(s[i:i+2])+int(s[i+2]), int(s[i])+int(s[i+1])+int(s[i+2])]
            return (vals,j)
        
        @lru_cache(None)
        def f(x,y,residue): #x, y are index of s1 and s2, respectively, residue is the unmatched characters left, if positive, s1 has unmatched, if negative, s2 has unmathced chars
            if x==len(s1) and y==len(s2) and residue==0:
                return True
            if x==len(s1) and y==len(s2):
                return False
            if x==len(s1) and residue<=0:
                return False
            if y==len(s2) and residue>=0:
                return False
            if residue==0:
                if s1[x].isalpha() and s2[y].isalpha():
                    return s1[x]==s2[y] and f(x+1, y+1, 0)
                elif s2[y].isalpha():
                    vals, j = getVals(0,x)
                    for v in vals:
                        if f(j,y+1,v-1): return True
                    return False
                elif s1[x].isalpha():
                    vals, j = getVals(1,y)
                    for v in vals:
                        if f(x+1,j,1-v): return True
                    return False
                else:
                    vals1, j1 = getVals(0,x)
                    vals2, j2 = getVals(1,y)
                    for v1 in vals1:
                        for v2 in vals2:
                            if f(j1, j2, v1-v2): return True
                    return False
            elif residue>0:
                if s2[y].isalpha():
                    return f(x,y+1, residue-1)
                else:
                    vals, j = getVals(1,y)
                    for v in vals:
                        if f(x,j,residue-v): return True
                    return False
            else:
                if s1[x].isalpha(): return f(x+1,y,residue+1)
                else:
                    vals, j = getVals(0,x)
                    for v in vals:
                        if f(j,y, residue+v): return True
                    return False
            
        return f(0,0,0)
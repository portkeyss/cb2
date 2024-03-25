class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        m1, m2 = len(encoded1), len(encoded2)
        i = 0
        j = 0
        res = []
        while i<m1:
            a = encoded1[i][0]*encoded2[j][0]
            b = min(encoded1[i][1],encoded2[j][1])
            if res and res[-1][0]==a:
                res[-1][1] += b
            else:
                res.append([a,b])    
            if encoded1[i][1]<encoded2[j][1]:
                encoded2[j][1] -= encoded1[i][1]
                i += 1
            elif encoded1[i][1]>encoded2[j][1]:
                encoded1[i][1] -= encoded2[j][1]
                j += 1
            else:
                i += 1
                j += 1
        return res
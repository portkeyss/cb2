class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        res = []
        freq = dict()
        for name in names:
            if name not in freq:
                res.append(name)
                freq[name] = 1
            else:
                a = name
                k = freq[name]
                while True:
                    a = name+"("+str(k)+")"
                    if a in freq:
                        k += 1
                    else:
                        break
                res.append(a)
                freq[name] = k
                freq[a] = 1
        return res
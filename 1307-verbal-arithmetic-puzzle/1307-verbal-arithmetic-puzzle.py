class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        words = [word[::-1] for word in words]
        result = result[::-1]
        chars = set(c for w in words+[result] for c in w)
        n = len(words)
        m = max(len(word) for word in words)
        l = len(result)
        if m>l: return False
        
        c2i = dict()
        i2c = dict()
        
        def f(bit,wordIdx,sm):
            if bit==l:
                return sm==0
            elif wordIdx==n:
                if sm==0 and l>1 and bit==l-1: return False
                a, b = sm%10, sm//10
                if a in i2c:
                    if i2c[a]==result[bit]: return f(bit+1,0,b)
                    else: return False
                elif result[bit] in c2i:
                    if c2i[result[bit]]==a: return f(bit+1,0,b)
                    else: return False
                else:
                    i = a
                    ch = result[bit]
                    i2c[i] = ch
                    c2i[ch] = i
                    if f(bit+1,0,b): return True
                    else:
                        i2c.pop(i)
                        c2i.pop(ch)
            elif bit>=len(words[wordIdx]):
                return f(bit, wordIdx+1, sm)
            elif words[wordIdx][bit] in c2i:
                i = c2i[words[wordIdx][bit]]
                if i==0 and len(words[wordIdx])>1 and bit==len(words[wordIdx])-1: return False
                return f(bit, wordIdx+1, sm+i)
            else:
                ch = words[wordIdx][bit]
                for i in range(10):
                    if i in i2c or i==0 and len(words[wordIdx])>1 and bit==len(words[wordIdx])-1:
                        continue
                    i2c[i] = ch
                    c2i[ch] = i
                    if f(bit, wordIdx+1, sm+i): return True
                    else:
                        i2c.pop(i)
                        c2i.pop(ch)
                return False
            
        return f(0,0,0)
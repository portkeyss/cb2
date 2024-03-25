class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        buffer = []
        for i,c in enumerate(word):
            if c.isalpha():
                if i>0 and word[i-1].isnumeric():
                    buffer.append(" ")   
            else:
                buffer.append(c)
        if not buffer: return 0
        if buffer[-1]==" ": buffer.pop()
        l = "".join(buffer)
        p = l.split(" ")
        
        def trim(s):
            i = 0
            while i<len(s)-1 and s[i]=="0":
                i += 1
            return s[i:]

        return len(set(trim(x) for x in p))
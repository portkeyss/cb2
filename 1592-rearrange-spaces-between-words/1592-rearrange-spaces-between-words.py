class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = []
        spaces = 0
        wordStart = -1
        for i in range(len(text)):
            if text[i]==" ":
                if wordStart>=0: 
                    words.append(text[wordStart:i])
                wordStart = -1
                spaces += 1
            else:
                if i==0 or text[i-1]==" ":
                    wordStart = i
        if wordStart>=0:
            words.append(text[wordStart:])
        wordCount = len(words)
        if wordCount==1: return words[0]+" "*spaces
        x, y = spaces//(wordCount-1), spaces%(wordCount-1)
        return (" "*x).join(words)+" "*y
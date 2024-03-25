class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m,n = len(word1),len(word2)
        i = j = 0
        buffer = []
        flag = True
        while i<m and j<n:
            if flag:
                buffer.append(word1[i])
                i += 1
            else:
                buffer.append(word2[j])
                j += 1
            flag = not flag
        if i<m: buffer.append(word1[i:])
        elif j<n: buffer.append(word2[j:])
        return "".join(buffer)
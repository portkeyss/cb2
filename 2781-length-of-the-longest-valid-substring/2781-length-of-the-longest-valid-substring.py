class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)
        p = max(len(w) for w in forbidden)
        x = 0
        ans = 0
        for i in range(len(word)):
            j = i
            k = max(i-x,i-p+1)
            while j>=k:
                if word[j:i+1] in forbidden:
                    x = i-j
                    break
                j -= 1
            if j<k: x += 1
            ans = max(ans, x)
        return ans       
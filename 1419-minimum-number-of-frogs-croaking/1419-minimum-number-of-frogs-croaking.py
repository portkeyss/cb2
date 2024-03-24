class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        frogs = 0
        activefrogs = 0
        activeCount = Counter()
        for c in croakOfFrogs:
            if c == "c":
                activefrogs += 1
                activeCount[c] += 1
                frogs = max(frogs, activefrogs)
            elif c == "r":
                if activeCount["c"] > 0:
                    activeCount["c"] -= 1
                    activeCount["r"] += 1
                else:
                    return -1
            elif c == "o":
                if activeCount["r"] > 0:
                    activeCount["r"] -= 1
                    activeCount["o"] += 1
                else:
                    return -1
            elif c == "a":
                if activeCount["o"] > 0:
                    activeCount["o"] -= 1
                    activeCount["a"] += 1
                else:
                    return -1
            elif c == "k":
                if activeCount["a"] > 0:
                    activeCount["a"] -= 1
                    activefrogs -= 1   
                else:
                    return -1     
        return frogs if sum(activeCount.values()) == 0 else -1
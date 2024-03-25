class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return sum(ruleKey=="type" and ruleValue==t or ruleKey=="color" and ruleValue==c or ruleKey == "name" and ruleValue==n for t,c,n in items)
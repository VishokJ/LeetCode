class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.processString(s) == self.processString(t)
    
    def processString(self, s):
        final = ""
        for i in list(s):
            if i == "#": final = final[:-1]
            else: final += i
        return final
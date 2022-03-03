class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.processString(s) == self.processString(t)
    
    def processString(self, s):
        listS = []
        for i in list(s):
            if i == "#": 
                 if len(listS): listS.pop() # Need to put two if's to make sure to not put '#' in list
            else: listS.append(i)
        print(listS)
        return listS
class Solution(object):
    def plusOne(self, digits):
        newDig = []
        plus = True
        for i in reversed(range(len(digits))):
            if plus:
                if digits[i] >= 9:
                    if len(digits) == 1: newDig.insert(0, 0)
                    if i == 0:
                        newDig.insert(0, 1)
                        plus = False
                    else:
                        newDig.insert(0, digits[i] % 9)
                        digits[i-1] += 1
                        plus = False
                else:
                    newDig.insert(0, digits[i]+1)
                    plus = False
            else:
                if digits[i] > 9:
                    newDig.insert(0, digits[i] % 10)
                    if i == 0: newDig.insert(0, 1)
                    else: digits[i-1]+=1
                else: newDig.insert(0, digits[i])
        return newDig
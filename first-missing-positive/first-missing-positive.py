class Solution(object):
    def firstMissingPositive(self, nums):
        newNums = sorted(list(set([i for i in nums if i >= 1])))
        print(newNums)
        if len(newNums) == 1:
            if newNums[0] == 1: return 2
            return 1
        for i in range(len(newNums)):
            if i+1 != newNums[i]: return i+1
        return len(newNums)+1
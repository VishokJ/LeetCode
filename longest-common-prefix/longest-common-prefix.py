class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0: return ""
        preStr = strs[0]
        count = len(preStr)
        for i in strs:
            if count > len(i):
                count = len(i)
                preStr = preStr[:count]
            while preStr != i[:count]:
                count -= 1
                preStr = preStr[:count]
        return preStr

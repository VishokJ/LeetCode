class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = "aeiou"
        currVal = 0
        for i in range(k):
            if s[i] in vowels:
                currVal += 1  
        maxVal = currVal
        
        for i in range(k, len(s)):
            if (s[i] in vowels): currVal += 1
            if (s[i-k] in vowels): currVal -= 1
            if (currVal > maxVal): maxVal = currVal
        
        return maxVal

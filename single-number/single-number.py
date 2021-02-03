class Solution(object):
    def singleNumber(self, nums):
        h = set()
        for i, num in enumerate(nums):
            if num in h:
                h.discard(num)
            else: h.add(num)
        return h.pop()
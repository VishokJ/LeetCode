class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums)) != len(nums)
        valMap = {}
        for i, n in enumerate(nums):
            if n in valMap: return True
            valMap[n] = i
        return False
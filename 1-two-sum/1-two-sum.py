class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valMap = {}
        for i, n in enumerate(nums):
            if target - n in valMap: return [i, valMap[target - n]]
            valMap[n] = i
        return
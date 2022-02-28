class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        startIndex = 0
        endIndex = len(nums)-1
        while startIndex <= endIndex and not(nums[startIndex] == target and nums[endIndex] == target):
            if nums[startIndex] < target:
                startIndex += 1
            if nums[endIndex] > target:
                endIndex -= 1
        if startIndex > endIndex: return [-1, -1]
        return [startIndex, endIndex]
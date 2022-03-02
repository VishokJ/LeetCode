class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if (target - nums[i]) in nums[:i]+nums[i+1:]:
                return [i, len(nums) - nums[::-1].index(target - nums[i]) - 1]
        
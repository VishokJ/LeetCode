class Solution(object):
    def permute(self, nums):
        arrList = []
        permList = []
        if len(nums) <= 1: return [nums]
        if len(nums) == 2: return [[nums[0], nums[1]], [nums[1], nums[0]]]
        for i in range(len(nums)):
            arrList.append(nums[i:len(nums)]+nums[0:i])
        for i in arrList:
            for x in self.permute(i[:-1]):
                x.append(i[-1])
                permList.append(x)
        return permList
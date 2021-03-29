class Solution(object):
    def permuteUnique(self, nums):
        arrList = []
        final = []
        permList = []
        if len(nums) <= 1: return [nums]
        if len(nums) == 2:
            permList = [[nums[0], nums[1]], [nums[1], nums[0]]]
            [final.append(x) for x in permList if x not in final]
            return final
        for i in range(len(nums)):
            if nums[i:]+nums[0:i] not in arrList:
                arrList.append(nums[i:]+nums[0:i])
        for i in arrList:
            for x in self.permuteUnique(i[:-1]):
                x.append(i[-1])
                permList.append(x)
        [final.append(x) for x in permList if x not in final]
        return final
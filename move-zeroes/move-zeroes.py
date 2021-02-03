class Solution(object):
    def moveZeroes(self, nums):
        for i, num in enumerate(nums):
            if num == 0:
                nums.remove(0)
                nums.append(0)
        return nums
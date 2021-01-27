class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3: return []
        output = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: continue
            start = i + 1
            end = len(nums) - 1
            while start < end:
                total = nums[start]+nums[end]+a
                if total == 0:
                    b = [nums[start],nums[end],a]
                    if b not in output:
                        output.append(b)
                if total > 0:
                    end -= 1
                else: start += 1
        return output

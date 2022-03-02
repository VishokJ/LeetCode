class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sols = []
        if len(nums) < 3: return sols
        nums.sort()
        dictSums = {}
        for i in range(len(nums)-1):
            if i > 0 and nums[i - 1] == nums[i]: continue # Skipping if the number is a duplicate
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < -nums[i]:
                    l += 1
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
                else:
                    sols.append([nums[l], nums[r], nums[i]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return sols
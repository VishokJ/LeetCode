class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = sys.maxsize
        for i, n in enumerate(nums):            
            if i > 0 and nums[i-1] == n: continue
            l, r = i+1, len(nums)-1
            while l < r:
                #print(n, nums[l], nums[r])
                threeSum = n + nums[l] + nums[r]
                #print(threeSum)
                if threeSum > target: r -= 1
                elif threeSum < target: l += 1
                else: return threeSum
                if abs(threeSum - target) < abs(closest - target):
                    closest = threeSum
        return closest
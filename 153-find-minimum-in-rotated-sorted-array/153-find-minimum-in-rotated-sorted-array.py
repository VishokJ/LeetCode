class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            print(nums[l:r+1])
            m = (l + r) // 2
            if (m == len(nums) - 1 or nums[m] < nums[m + 1]) and (m == 0 or nums[m] < nums[m - 1]):
                return nums[m]
            elif nums[l] <= nums[m]:
                if nums[l] <= nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[l] >= nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
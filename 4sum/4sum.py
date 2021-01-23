class Solution(object):
    def fourSum(self, nums, target):
        #Two loops of two pointers each.
        if len(nums) < 4: return []
        nums.sort()
        start = 0
        end = len(nums) - 1
        output = []
        for start in range(0, len(nums)-1):
            for end in range(start+1, len(nums)-1):
                otherNums = nums[:start] + nums[start+1:end] + nums[end+1:]
                sumOne = nums[start] + nums[end]
                startTwo = 0
                endTwo = len(otherNums) - 1
                while endTwo > startTwo:
                    sumTwo = otherNums[startTwo] + otherNums[endTwo]
                    if sumOne + sumTwo == target:
                        n = sorted([nums[start], nums[end], otherNums[startTwo], otherNums[endTwo]])
                        if n not in output: output.append(n)
​
                    if sumOne + sumTwo > target:
                        endTwo -= 1
                    else: startTwo += 1
        return output

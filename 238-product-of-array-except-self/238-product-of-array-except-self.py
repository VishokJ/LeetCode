class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]
        pre = 1
        post = 1
        for n in nums[:len(nums)-1]:
            pre *= n
            prefix.append(pre)
        for n in range(len(nums)-1, 0, -1):
            post *= nums[n]
            postfix.append(post)
        
        postfix = postfix[::-1]
        return([prefix[i] * postfix[i] for i in range(len(prefix))])
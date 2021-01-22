class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = 0
        b = len(numbers) - 1
        while b > a:
            if numbers[a] + numbers[b] == target:
                break
            elif numbers[a] + numbers[b] > target:
                b = b - 1
            else: a = a + 1
        return [a+1, b+1]

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        areas = []
        start = 0
        end = len(height)-1
        while (start < end):
            area = min(height[start], height[end]) * (end - start)
            areas.append(area)
            if (height[start] >= height[end]): end = end - 1
            else: start = start + 1
        return max(areas)

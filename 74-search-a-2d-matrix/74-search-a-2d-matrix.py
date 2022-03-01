class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        firstCol = [a[0] for a in matrix]
        arrIndex = self.binSearch(firstCol, target)
        arr = matrix[arrIndex]
        return (arr[self.binSearch(arr, target)] == target)
        
    def binSearch(self, arr, target):
        l, r = 0, len(arr) - 1
        m = 0
        while (l <= r):
            m = (l + r) // 2
            if (arr[m] < target):
                l = m + 1;
            elif (arr[m] > target):
                r = m - 1;
            else:
                return m;
        return l - 1;
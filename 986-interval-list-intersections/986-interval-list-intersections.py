class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        outList = []
        s = t = 0
        while s < len(firstList) and t < len(secondList):
            start = max(firstList[s][0], secondList[t][0])
            end = min(firstList[s][1], secondList[t][1])
            if start <= end:
                outList.append([start, end])
                if end == firstList[s][1]: s += 1
                else: t += 1
            else:
                if start == firstList[s][0]: t += 1
                else: s += 1
        return outList
from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        

        i, j = 0, 0
        res = []

        while i < len(firstList) and j < len(secondList):

            if firstList[i][0] > secondList[j][1]:
                j += 1
                continue

            if secondList[j][0] > firstList[j][1]:
                i += 1
                continue

            if firstList[i][1] <= secondList[j][1]:
                if firstList[i][0] > secondList[j][0]:
                    res.append([firstList[i][0], firstList[i][1]])
                else:
                    res.append([secondList[j][0], firstList[i][1]])

                i += 1
            elif firstList[i][1] >= secondList[j][1]:
                if firstList[i][0] < secondList[j][0]:
                    res.append([secondList[j][0], secondList[j][1]])
                else:
                    res.append([firstList[i][0], secondList[j][1]])

                j += 1

        return res
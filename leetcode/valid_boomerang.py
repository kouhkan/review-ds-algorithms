from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        l = []
        for point in points:
            diff = point[0] - point[1]

            if diff == 0:
                l.append(True)
            else:
                l.append(False)

        while l:
            if l.pop() == False:
                return True
        return False



s = Solution()
print(s.isBoomerang([[1,1],[2,3],[3,2]]))

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}

        for num in nums:
            d[num] = 0

        for num in nums:
            d[num] += 1

        for num in d:
            if d[num] == max(d.values()):
                return num


s = Solution()
s.majorityElement([3, 2, 3])

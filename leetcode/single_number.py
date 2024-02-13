from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}

        for num in nums:
            d[num] = 0

        for num in nums:
            d[num] += 1

        for k, v in d.items():
            if d[k] == 1:
                return k


s = Solution()
print(s.singleNumber([1]))

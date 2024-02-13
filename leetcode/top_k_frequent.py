from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for n in nums:
            d[n] = 0

        for n in nums:
            d[n] += 1

        s = sorted(d.values(), reverse=True)[:k]

        l = []
        for i in d:
            if d[i] in s:
                l.append(i)

        return l





s = Solution()
s.topKFrequent([1], 1)

class Solution:
    def isUgly(self, n: int) -> bool:
        for i in range(2, n):
            if n % i == 0:
                return True
        else:
            return False


s = Solution()
print(s.isUgly(14))

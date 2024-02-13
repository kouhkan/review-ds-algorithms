class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        # Initialize an array to store the number of ways to reach each step
        dp = [0] * (n + 1)

        # Base cases
        dp[1] = 1  # There's only one way to reach the first step
        dp[2] = 2  # There are two ways to reach the second step

        # Calculate the number of ways to reach each step using dynamic programming
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # The number of ways to reach the top is stored in dp[n]
        return dp[n]


s = Solution()
print(s.climbStairs(5))

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ""
        for i in s:
            if i.isalnum():
                ns += i.lower()

        return ns == ns[::-1]


s = Solution()
print(s.isPalindrome("0P0"))
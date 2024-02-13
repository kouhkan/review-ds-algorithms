class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        s = s[:k]
        return " ".join(s)

s = Solution()
print(s.truncateSentence("Hello how are you Contestant", 4))
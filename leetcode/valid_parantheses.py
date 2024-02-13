class Solution:
    def isValid(self, s: str) -> bool:
        l: list = []
        i = 0

        while i < len(s):
            l.append(s[i])
            i += 1

        h = []
        if l[-1] == "{" or l[-1] == "[" or l[-1] == "(":
            return False

        for i in range(len(l) - 1, -1, -1):
            if l[i] == ")" and l[i - 1] == "(":
                h.append(True)
            elif l[i] == "}" and l[i - 1] == "{":
                h.append(True)
            elif l[i] == "]" and l[i - 1] == "[":
                h.append(True)

        return any(h)


s = Solution()
s.isValid("(){}}{")

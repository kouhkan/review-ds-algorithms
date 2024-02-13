from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l = []
        i = 0

        while i < len(operations):
            if operations[i] != "D" and operations[i] != "C" and operations[i] != "+":
                l.append(int(operations[i]))
            elif operations[i] == "C":
                l.remove(l[-1])
            elif operations[i] == "D":
                l.append(l[-1] * 2)
            elif operations[i] == "+":
                l.append(l[-1] + l[-2])
            i += 1

        return sum(l)

s = Solution()
s.calPoints(["5", "2", "C", "D", "+"])

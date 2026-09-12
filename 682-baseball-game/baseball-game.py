class Solution(object):
    def calPoints(self, operations):
        ans = []
        for i in operations:
            if i.isdigit() or (i.startswith('-') and i[1:].isdigit()):
                ans.append(int(i))
            elif i == "+":
                ans.append(ans[-1] + ans[-2])
            elif i == "D":
                ans.append(2 * ans[-1])
            elif i == "C":
                ans.pop()
        return sum(ans)

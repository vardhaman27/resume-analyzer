class Solution(object):
    def maxDepth(self, s):
        stack = []
        curr = 0
        max_dept = 0
        for i in s:
            if i == "(":
                curr += 1
                max_dept = max(max_dept, curr)
            elif i == ")":
                curr -= 1

        return max_dept


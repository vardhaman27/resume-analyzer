class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            i = 0
            lst = []
            while i < len(s):
                ans = 0
                count = k
                while count > 0 and i < len(s):
                    ans += int(s[i])
                    count -= 1
                    i += 1
                lst.append(str(ans))
            s = "".join(lst)
        return s
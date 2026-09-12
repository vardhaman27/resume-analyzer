class Solution(object):
    def removeOuterParentheses(self, s):
        count = 0
        i = 0
        result = ""
        while i < len(s):
            if s[i] == "(" :
                count += 1
                if count > 1:
                    result += s[i]
                i +=1
            else:
                count -= 1
                if count > 0:
                    result += s[i]
                i += 1
        return result

        
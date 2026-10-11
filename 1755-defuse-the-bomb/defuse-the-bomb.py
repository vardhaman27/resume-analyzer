class Solution(object):
    def decrypt(self, code, k):
        arr = [0]
        if k == 0:
            return arr * len(code)
        temp =  code
        code = code*2
        for i in range(len(temp)):
            if  k > 0:
                temp[i] = sum(code[i + 1 : i+k+1])
            else:
                temp[i] = sum(code[i + len(temp)+k : i+len(temp)])
        return temp
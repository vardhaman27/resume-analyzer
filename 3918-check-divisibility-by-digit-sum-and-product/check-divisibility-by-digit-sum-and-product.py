class Solution(object):
    def checkDivisibility(self, n):
        x = n
        summ = 0
        prod = 1
        while x > 0:
            val = (x % 10)
            prod *= val
            summ += val
            x //= 10
        if n % (summ + prod)== 0:
            return True
        else:
            return False



        
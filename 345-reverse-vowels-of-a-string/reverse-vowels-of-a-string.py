class Solution(object):
    def reverseVowels(self, s):
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        l = []
        for i in s:
            if i in vowels:
                l.append(i)
        s = list(s)
        
        for x in range (len(s)):
            if s[x] in vowels:
                s[x] = l.pop()
        return "".join(s)

            
                
                


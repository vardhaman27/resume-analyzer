class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        sets = {}
        sett = {}
        for i in range (len(s)):
            if s[i] in sett:
                if sett[s[i]] != t[i]:
                    return False
            else:
                sett[s[i]] = t[i]
            if t[i] in sets:
                if sets[t[i]] != s[i]:
                    return False
            else:
                sets[t[i]] = s[i]
        return True
            
                
            



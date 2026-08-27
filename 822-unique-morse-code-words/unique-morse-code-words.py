class Solution(object):
    def uniqueMorseRepresentations(self, words):
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        org = []
        for word in words:
            result = ""
            for letter in word:
                index = ord(letter) - ord('a')
                result += code[index]
            org.append(result)
            
        unique = set(org)
        return len(unique)

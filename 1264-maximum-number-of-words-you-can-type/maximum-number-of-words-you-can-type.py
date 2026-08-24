class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        broken_letters = set(brokenLetters)
        words = text.split(" ")
        word_dict = {index : word for index, word in enumerate(words)}
        c = 0
        for index,i in word_dict.items():
            b = any(ch in broken_letters for ch in i)
            if not b:
                c+=1
        return c


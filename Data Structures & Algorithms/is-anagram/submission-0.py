class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = {}
        word2 = {}

        for ch in s:
            if ch not in word1.keys():
                word1[ch] = 1
            else:
                word1[ch] += 1
        
        for ch in t:
            if ch not in word2.keys():
                word2[ch] = 1
            else:
                word2[ch] += 1

        if word1.keys() != word2.keys():
            return False

        for key in word1.keys():
            if word1[key] != word2[key]:
                return False

        return True
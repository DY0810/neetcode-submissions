class Solution:
    def isDecomposable(self, s: str) -> bool:
        i = 0
        pair = 0 
        while i < len(s):
            j = i + 1
            while j < len(s) and s[i] == s[j]:
                j += 1
            
            if (j - i) % 3 == 2:
                pair += 1
            elif (j - i) % 3 == 1:
                return False
            i = j
        
        return pair == 1

            
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        ans = float('inf')
        i1 = i2 = -1
        same = word1 == word2

        for i, w in enumerate(wordsDict):
            if w == word1:
                if same:
                    if i1 != -1:
                        ans = min(ans, i - i1)
                    i1 = i
                    continue
                i1 = i
            elif w == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                ans = min(ans, abs(i1 - i2))

        return ans
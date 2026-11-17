class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = wordsDict

    def shortest(self, word1: str, word2: str) -> int:
        idx1 = 0
        idx2 = 0
        best = len(self.wordsDict)
        seen1 = False
        seen2 = False
        for i in range(len(self.wordsDict)):
            if self.wordsDict[i] == word1:
                idx1 = i
                seen1 = True
                if seen1 and seen2:
                    best = min(best, abs(idx1 - idx2))
                    seen2 = False
            elif self.wordsDict[i] == word2:
                idx2 = i
                seen2 = True
                if seen1 and seen2:
                    best = min(best, abs(idx1 - idx2))
                    seen1 = False

        return best
            


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
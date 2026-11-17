class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        best = len(wordsDict) - 1
        seen1 = False
        seen2 = False
        prev = -1
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                if word1 == word2:
                    if prev == -1:
                        prev = i
                    else:
                        best = min(best, abs(i - prev))
                        prev = i
                else:
                    seen1 = True
                    idx1 = i
                if seen1 and seen2:
                    best = min(best, abs(idx1 - idx2))

            elif wordsDict[i] == word2:
                seen2 = True
                idx2 = i
                if seen1 and seen2:
                    best = min(best, abs(idx1 - idx2))

        return best
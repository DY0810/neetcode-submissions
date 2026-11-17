from collections import defaultdict
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        best = len(wordsDict) - 1
        seen1 = False
        seen2 = False
        if word1 == word2:
            for i in range(len(wordsDict)):
                if wordsDict[i] == word1 and not seen1:
                    seen1 = True
                    idx1 = i
                    if seen1 and seen2:
                        best = min(best, abs(idx1 - idx2))
                        seen2 = False

                elif wordsDict[i] == word2 and not seen2:
                    seen2 = True
                    idx2 = i
                    if seen1 and seen2:
                        best = min(best, abs(idx1 - idx2))
                        seen1 = False
        else:
            positions = defaultdict(list)
            for i, word in enumerate(wordsDict):
                positions[word].append(i)
            
            i = j = 0
            list1 = positions[word1]
            list2 = positions[word2]

            while i < len(list1) and j < len(list2):
                best = min(best, abs(list1[i] - list2[j]))
                if list1[i] < list2[j]:
                    i += 1
                else:
                    j += 1        
        return best
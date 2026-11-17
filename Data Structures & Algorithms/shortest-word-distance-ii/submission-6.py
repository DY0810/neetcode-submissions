class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.positions = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.positions[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        list1 = self.positions[word1]
        list2 = self.positions[word2]
        i = j = 0
        best = float('inf')

        while i < len(list1) and j < len(list2):
            best = min(best, abs(list1[i] - list2[j]))
            if list1[i] < list2[j]:
                i += 1
            else:
                j+= 1
        
        return best


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
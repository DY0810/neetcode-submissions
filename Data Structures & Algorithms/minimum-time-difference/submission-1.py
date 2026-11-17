class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0

        seen = [False] * 1440

        for t in timePoints:
            n = int(t[0:2]) * 60 + int(t[3:])
            if seen[n]:
                return 0
            else:
                seen[n] = True

        best = 1440
        prev = -1
        for i in range(1440):
            if seen[i] and prev == -1:
                prev = i
                start = i
            elif seen[i]:
                best = min(best, i - prev)
                prev = i
        
        return min(best, start + 1440 - prev)
        
            
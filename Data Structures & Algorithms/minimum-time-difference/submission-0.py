class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0

        seen = [False] * 1440
        times = []

        for t in timePoints:
            n = int(t[0:2]) * 60 + int(t[3:])
            if seen[n]:
                return 0
            else:
                seen[n] = True
                times.append(n)

        times.sort()
        best = 1440

        for i in range(len(times) - 1):
            best = min(best, times[i+1] - times[i])

        return min(best, times[0] + 1440 - times[-1])
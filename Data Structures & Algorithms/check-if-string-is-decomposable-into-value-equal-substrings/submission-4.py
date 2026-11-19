class Solution:
    def isDecomposable(self, s: str) -> bool:
        n = len(s)
        dp0 = [False] * (n + 1)
        dp1 = [False] * (n + 1)
        dp0[0] = True
        for i in range(1, n + 1):
            if i >= 3 and s[i - 3] == s[i - 2] == s[i - 1]:
                dp0[i] = dp0[i] or dp0[i - 3]
                dp1[i] = dp1[i] or dp1[i - 3]
            if i >= 2 and s[i - 2] == s[i - 1]:
                dp1[i] = dp1[i] or dp0[i - 2]
        return dp1[n]
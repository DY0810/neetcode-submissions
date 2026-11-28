class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        best = 0

        for n in nums:
            if n - 1 in seen:
                continue
            length = 1
            while n + length in seen:
                length += 1
            best = max(best, length)
        
        return best
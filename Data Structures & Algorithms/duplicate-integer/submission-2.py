class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = {}
        for n in nums:
            if n in tracker.keys():
                return True
            else:
                tracker[n] = 1
        return False
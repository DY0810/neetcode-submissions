class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = {}
        for n in nums:
            if n not in tracker.keys():
                tracker[n] = 1
            else:
                return True
        return False
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}

        for i in range(len(nums)):
            tracker[nums[i]] = i
        
        for i, n in enumerate(tracker):
            if target - n in tracker and tracker[target - n] != i:
                return [i, tracker[target - n]]
        
        return []
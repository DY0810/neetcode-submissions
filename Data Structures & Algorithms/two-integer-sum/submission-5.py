class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}

        for i in range(len(nums)):
            tracker[nums[i]] = i
        
        """
        This one needs enumerate because without it target[5] will always return 0
        for edge cases like nums = [5,5]
        """
        for i, n in enumerate(tracker):
            if target - n in tracker and tracker[target - n] != i:
                return [i, tracker[target - n]]

        return []
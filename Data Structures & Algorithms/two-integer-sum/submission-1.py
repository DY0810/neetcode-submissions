class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}

        for i, n in enumerate(nums):
            print(i, n)
            tracker[n] = i
        
        for i, n in enumerate(tracker):
            print(i, n)
            if target - n in tracker and tracker[target - n] != i:
                return [i, tracker[target - n]]
        
        return []




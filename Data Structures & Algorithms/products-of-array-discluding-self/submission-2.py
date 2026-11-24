class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[2, 3, 5, 8, 4]
        #[2, 2, 6, 30, 240]
        #[480, 320, 192, 120, 240]
        product = nums[0]
        res = [nums[0]]
        for i in range(1, len(nums)):
            temp = nums[i]
            res.append(product)
            product *= temp
        
        product = nums[-1]
        for j in range(len(nums) - 2, 0, -1):
            temp = nums[j]
            res[j] *= product
            product *= temp
        res[0] = product
        
        return res
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        prev = 1
        for i in range(1, len(nums)):
            prev *= nums[i-1]
            prefix[i] = prev
        prev = 1
        for i in range(len(nums)-2, -1 , -1):
            prev *= nums[i+1]
            suffix[i] = prev
        return [prefix[i] * suffix[i] for i in range(len(nums))]

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxval, track = nums[0], nums[0]
        for n in range(1, len(nums)):
            track = max(nums[n], track + nums[n])
            maxval = max(maxval, track)
        return maxval

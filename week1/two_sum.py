class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if (nums[i]) in d.keys():
                return [d[nums[i]][0],i]
            else:
                d[target - nums[i]] = [i]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = set()
        for i in range(len(nums)):
            target = -1 * nums[i]
            d = {}
            if not (i > 0 and nums[i] == nums[i-1]):
                for j in range(len(nums)):
                    if j != i:
                        if nums[j] in d:
                            ans = tuple(sorted([nums[i], nums[d[nums[j]]], nums[j]]))
                            out.add(ans)
                        else:
                            d[target-nums[j]] = j
        return [list(a) for a in out]

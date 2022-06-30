class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length=len(nums)
        start=0
        ans=-1e5
        for i in range(0,len(nums)):
            start+=nums[i]
            ans=max(start,ans)
            if start<0:
                start=0
        return ans
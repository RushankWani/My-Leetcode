class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        set1=set()
        x=len(nums)//2
        minimum=nums[:x]
        maximum=nums[x:]
        for i in range(x):
            set1.add(minimum[i]+maximum[x-i-1])
        return max(set1)
        
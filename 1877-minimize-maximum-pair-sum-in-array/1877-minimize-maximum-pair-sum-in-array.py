class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        list=[]
        x=len(nums)//2
        minimum=nums[:x]
        maximum=nums[x:]
        for i in range(x):
            list.append(minimum[i]+maximum[x-i-1])
        return max(list)
        
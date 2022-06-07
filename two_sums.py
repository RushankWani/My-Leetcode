class Solution(object):
    def twoSum(self, nums, target):
        a=[]
        for x in range(0,len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x]+nums[y]==target:
                    return x,y

obj=Solution()
obj.twoSum([2,7,11,15],9)
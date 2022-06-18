class Solution(object):
    def runningSum(self, nums):
        for i in range(1,len(nums)):
            for j in range(0,len(nums)):
                nums[i]=nums[i] + nums[i-1]
                break
        return nums
        
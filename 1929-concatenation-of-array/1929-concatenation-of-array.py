class Solution(object):
    def getConcatenation(self, nums):
        for i in range(0,len(nums)):
            nums.append(nums[i])
        return nums
        
        
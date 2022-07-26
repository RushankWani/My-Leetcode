class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)+1):
            count+=i
        return count-sum(nums)
        
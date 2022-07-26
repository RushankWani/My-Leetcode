class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totl = (n+1)*n//2
        s = sum(nums)
        return totl-s


        
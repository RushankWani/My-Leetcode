class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        mid=len(nums)//2
        for i in nums:
            count+=abs(nums[mid]-i)
        return count
        
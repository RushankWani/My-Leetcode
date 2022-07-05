class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        else:
            nums.sort()
            longest_streak = 1
            current_streak = 1

            for i in range(1, len(nums)):
                if nums[i] != nums[i-1]:
                    if nums[i] == nums[i-1]+1:
                        current_streak += 1
                    else:
                        longest_streak = max(longest_streak, current_streak)
                        current_streak = 1

            return max(longest_streak, current_streak)

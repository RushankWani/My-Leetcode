class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for num in freq:
            count += (freq[num]*(freq[num]-1)//2)
        return count 
        
        
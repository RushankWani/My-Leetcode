class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        list=[]
        for i in range(0,len(nums)):
            count=0
            for j in nums:
                if nums[i]>j:
                    count+=1
            list.append(count)
        return list
        
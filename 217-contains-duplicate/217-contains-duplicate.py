class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1=set()
        for i in nums:
            set1.add(i)
        print(set1)
        diff=abs(len(set1)-len(nums))
        if diff>0:
            return True
        else:
            return False
        
        
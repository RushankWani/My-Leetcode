class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        gvar=0
        for i in nums:
            if i == 0:
                count=0
            else:
                count+=1
                if count>=gvar:
                    gvar=count
        return gvar
            
class Solution(object):
    def moveZeroes(self, nums):
        counter=0
        for i in nums:
            if i==0:
                counter=counter+1
        while counter!=0:
            nums.remove(0)
            nums.append(0)
            counter=counter-1
        return nums
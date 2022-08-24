class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hmap=dict()
        list=[]
        for i in nums:
            if i in hmap:
                hmap[i]+=1
            else:
                hmap[i]=1
        permit=len(nums)/3
        for ele,count in hmap.items():
            if count>permit:
                list.append(ele)
        return list
        
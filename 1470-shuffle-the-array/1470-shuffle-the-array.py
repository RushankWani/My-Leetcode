class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list1=nums[:n]
        list2=nums[n:]
        list=[]
        for l1,l2 in zip(list1,list2):
            list.append(l1)
            list.append(l2)
        return list
        
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # nums = [4,1,2,1,2]
        dict1=dict()
        for i in nums:
            count=1
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=count

        key_list = list(dict1.keys())
        val_list = list(dict1.values())

        position = val_list.index(1)
        return key_list[position]
            
        
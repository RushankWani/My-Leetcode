class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # dict1=dict()
        # for i in nums:
        #     count=1
        #     if i in dict1:
        #         dict1[i]+=count
        #     else:
        #         dict1[i]=count
        # kval=dict1.keys()
        # vval=dict1.values()
        # p=max(vval)
        # position=
        # return dict1[position]
        dict1=dict()
        for i in nums:
            count=1
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=count

        key_list = list(dict1.keys())
        val_list = list(dict1.values())

        position = val_list.index(max(val_list))
        return key_list[position]
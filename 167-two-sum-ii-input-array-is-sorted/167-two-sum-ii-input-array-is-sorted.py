class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict1={}
        for index,ele in enumerate(numbers,1):
                remain=target-ele
                if remain in dict1:
                    return [dict1[remain],index]
                dict1[ele]=index
        
        
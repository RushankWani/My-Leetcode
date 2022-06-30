class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr=[]
        arr.append(first)
        for i in range(0,len(encoded)):
            arr.append(encoded[i]^arr[-1])
        return arr
            
        
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict1=dict()
        for s in stones:
            count=1
            if s in dict1:
                dict1[s]+=count
            else:
                dict1[s]=count
        output=0
        for i in jewels:
            if i in dict1:
                output+=dict1[i]
        return output        
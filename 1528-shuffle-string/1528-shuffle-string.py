class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dict1={}
        op=""
        for i in range(len(s)):
            dict1[indices[i]]=s[i]
        for i in range(len(s)):
            op+=dict1[i]
        return op
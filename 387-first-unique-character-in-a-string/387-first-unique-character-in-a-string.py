class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1=dict()
        for ele in range(len(s)):
            if s[ele] not in dict1:
                dict1[s[ele]]=1
            else:
                dict1[s[ele]]= -1
        for i in range(len(s)):
            if dict1[s[i]]==1:
                return i
        return-1
            
class Solution:
    def romanToInt(self, s: str) -> int:
        dict1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        count=dict1[s[0]]
        prev=0
        for curr in range(1,len(s)):
            if dict1[s[prev]]>=dict1[s[curr]]:
                count+=dict1[s[curr]]
                prev+=1
            elif dict1[s[prev]]<dict1[s[curr]]:
                count-=dict1[s[prev]]
                count+=(dict1[s[curr]]-dict1[s[prev]])
                prev+=1
        return count
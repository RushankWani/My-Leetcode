class Solution:
    def balancedStringSplit(self, s: str) -> int:
        i=0
        back=0
        count=0
        lcount=0
        rcount=0
        while i!=len(s):
            if s[i]=="L":
                lcount+=1
            if s[i]=="R":
                rcount+=1
            if len(s[back:i+1])%2==0 and lcount==rcount:
                count+=1
                back=i+1
                lcount,rcount=0,0
            i+=1
        return count
        
        
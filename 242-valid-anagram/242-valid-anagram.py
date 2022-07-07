class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            dict1=dict()
            for ele in s:
                count=1
                if ele in dict1:
                    dict1[ele]+=1
                else:
                    dict1[ele]=count
            # print(dict1)
            for tele in t:
                if tele in dict1 and dict1[tele]>0:
                    dict1[tele]-=1
            print(dict1)
            for i in dict1:
                if dict1[i]>0:
                    return False
            return True

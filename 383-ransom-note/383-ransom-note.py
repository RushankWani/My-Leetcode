class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1=dict()
        for ele in magazine:
            count=1
            if ele in dict1:
                dict1[ele]+=1
            else:
                dict1[ele]=count
        print(dict1)
        for rele in ransomNote:
            if rele in dict1 and dict1[rele]>0:
                dict1[rele]-=1
            else:
                return False
        return True

        
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res=[]
        dictp=dict()
        listp=[]
        count=0
        for i in pattern:
            if i in dictp:
                listp.append(dictp[i])
            else:
                dictp[i]=count
                listp.append(dictp[i])
                count+=1
        # print(listp)
        for word in words:
            dictw=dict()
            listw=[]
            count1=0
            for letter in word:
                if letter in dictw:
                    listw.append(dictw[letter])
                else:
                    dictw[letter]=count1
                    listw.append(dictw[letter])
                    count1+=1
            # print(listw)
            if listp==listw:
                res.append(word)
        return res
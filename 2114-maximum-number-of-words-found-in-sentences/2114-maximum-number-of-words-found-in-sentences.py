class Solution(object):
    def mostWordsFound(self, sentences):
        list=[]
        for i in sentences:
            counter1=1
            for j in i:
                if j==" ":
                    counter1=counter1+1
            list.append(counter1)
        return max(list)
        
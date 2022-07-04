class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        list1=[]
        for i,row in enumerate(mat):
            for j,ele in enumerate(row):
                list1.append(int(ele))
        # print(list1)
        final=[]
        if r*c==len(list1) and r and c:
            count=0
            for x in range(1,r+1):
                local=[]
                for y in range(1,c+1):
                    local.append(list1[count])
                    count+=1
                final.append(local)
            return final
        else:
            return mat    